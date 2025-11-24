import streamlit as st # 导入 Streamlit 库，用于构建 Web 应用的界面
import pandas as pd # 导入 Pandas 库，用于数据处理和分析
import os # 导入 os 库，用于操作系统相关功能，例如检查文件是否存在

# 1. 页面配置 (Page Config) - Streamlit 规定必须是应用的第一个命令
st.set_page_config(
    page_title="Netflix Analytics Hub", # 设置浏览器标签页的标题
    page_icon="🎬", # 设置标签页的图标（Emoji）
    layout="wide", # 设置页面布局为宽屏模式，充分利用屏幕空间
    initial_sidebar_state="expanded" # 设置侧边栏初始状态为展开
)

# 2. 导入自定义模块
from utils import io, prep # 从 utils 包中导入 io（数据加载）和 prep（数据预处理）模块
from sections import intro, overview, deep_dives, conclusions # 从 sections 包中导入应用的四个页面模块

# 3. 常量定义：数据文件和 Logo 图片的文件名
DATA_PATH = 'Ntitles.csv' # 定义数据文件的路径
LOGO_2 = '微信图片_20251121083856_35_777.png' # 第一个 Logo 图片的文件名
LOGO_1 = 'retouch_2025112400100760.png' # 第二个 Logo 图片的文件名

def main():
    # --- 侧边栏用户界面 (Sidebar UI) ---
    
    # 调整 Logo 布局：通过注入 CSS 使两个 Logo 并排显示在侧边栏顶部
    st.sidebar.markdown("""
        <style>
            .sidebar-logo-container {
                display: flex; /* 启用 Flexbox 布局 */
                justify-content: space-between; /* 元素（图片）之间平均分配空间 */
                align-items: center; /* 垂直居中对齐 */
                margin-bottom: 1.5rem; /* 底部添加间距，与下方标题分隔 */
            }
            .sidebar-logo-container img {
                max-width: 48%; /* 限制每张图片的最大宽度，以确保两张图片都能并排显示 */
            }
        </style>
    """, unsafe_allow_html=True) # 允许 Streamlit 渲染包含自定义 CSS 的 HTML/Markdown
    
    # 使用自定义 HTML 容器的开始标签
    st.sidebar.markdown('<div class="sidebar-logo-container">', unsafe_allow_html=True)
    
    # Logo 1: 检查文件是否存在并显示
    if os.path.exists(LOGO_1): 
        st.sidebar.image(LOGO_1) # 在侧边栏显示 Logo 1
    
    # Logo 2: 检查文件是否存在并显示
    if os.path.exists(LOGO_2): 
        st.sidebar.image(LOGO_2) # 在侧边栏显示 Logo 2

    # 使用自定义 HTML 容器的结束标签
    st.sidebar.markdown('</div>', unsafe_allow_html=True)
    
    st.sidebar.title("Netflix Analytics") # 设置侧边栏的主要标题
    st.sidebar.caption("Strategic Content Intelligence") # 设置侧边栏的副标题
    st.sidebar.markdown("---") # 添加一条分隔线
    
    # 导航部分 (Navigation)
    page = st.sidebar.radio( # 创建单选按钮组，用于页面导航
        "Navigate", # 导航的标签名称
        ["Introduction", "Macro Overview", "Deep Dive Analysis", "Conclusions"], # 导航选项列表
        index=0 # 默认选中第一个选项（Introduction）
    )
    
    # --- 数据加载 (Data Loading) ---
    raw_df = io.load_data(DATA_PATH) # 调用 io 模块加载原始数据（使用了缓存）
    
    if raw_df.empty: # 检查数据框是否为空
        st.stop() # 如果为空，则停止应用执行
        
    df = prep.clean_data(raw_df) # 调用 prep 模块清洗数据，得到最终使用的数据框
    
    # --- 全局过滤器逻辑 (Global Filter Logic) ---
    # 仅在分析页面显示过滤器
    if page != "Introduction":
        st.sidebar.markdown("---") # 添加分隔线
        st.sidebar.subheader("🛠️ Filters") # 添加过滤器副标题
        
        # 过滤器 1: 内容类型 (Type)
        all_types = df['type'].unique().tolist() # 获取所有内容类型（Movie, TV Show）
        selected_types = st.sidebar.multiselect("Content Type", all_types, default=all_types) # 创建多选框
        
        # 过滤器 2: 年份范围 (Year Range)
        valid_years = df['added_year'].dropna() # 获取非空的添加年份
        if not valid_years.empty: # 确保有有效的年份数据
            min_year = int(valid_years.min()) # 数据集中的最小年份
            max_year = int(valid_years.max()) # 数据集中的最大年份
            default_start = 2015 if 2015 > min_year else min_year # 设置默认起始年份，确保不早于 2015 且不小于最小年份
            
            selected_years = st.sidebar.slider( # 创建滑块选择年份范围
                "Date Added Range",
                min_year, max_year, (default_start, max_year) # 默认选中从 default_start 到 max_year 的范围
            )
        else:
            selected_years = None # 如果没有有效年份数据，则设置为空
            
        # 过滤器 3: 主要制作国家 (Country)
        # 获取所有国家，排除 'Unknown'，并排序
        all_countries = sorted(list(set([c for c in df['primary_country'].unique() if c and c != 'Unknown'])))
        selected_countries = st.sidebar.multiselect("Primary Country", all_countries) # 创建多选框
        
        # 应用过滤器
        filtered_df = prep.filter_data(df, selected_types, selected_years, selected_countries) # 调用 prep 模块过滤数据
        
        # 显示当前筛选出的标题数量
        st.sidebar.info(f"Showing: {len(filtered_df)} titles")
    else:
        filtered_df = df # 如果在 Introduction 页面，则不过滤，使用全部数据

    # --- 学生信息 (Student Info) 在侧边栏底部 ---
    # 添加分隔线和间距，将信息推向底部
    st.sidebar.markdown("---")
    st.sidebar.markdown("<br>", unsafe_allow_html=True) 
    
    # 添加作者信息和 Github 链接（多行 Markdown 显示）
    st.sidebar.markdown(f"""
        **Course: Data Visualization 2025**                

        **Prof.Mano Mathew**
        
        **Author: Zhuoyang Xu**
        
        **Github:** [wake0506/Netflix-Analytics-Hub.git](https://github.com/wake0506/Netflix-Analytics-Hub.git)

        **Data sourse:Netflix Movies and TV Shows Comprehensive Catalogs(https://www.kaggle.com/datasets/kainatjamil12/niteee)**
    """)
    
    # --- 页面路由 (Page Routing) ---
    st.title("Netflix Content Strategy Report") # 设置主页面的主要标题
    
    if page == "Introduction": # 根据侧边栏的选择进行页面切换
        intro.show(df) # 显示 Introduction 页面内容，使用原始数据
    elif page == "Macro Overview": 
        overview.show(filtered_df) # 显示 Macro Overview 页面内容，使用过滤后的数据
    elif page == "Deep Dive Analysis": 
        deep_dives.show(filtered_df) # 显示 Deep Dive Analysis 页面内容，使用过滤后的数据
    elif page == "Conclusions": 
        conclusions.show() # 显示 Conclusions 页面内容

if __name__ == "__main__": # 检查是否作为主程序运行
    main() # 调用主函数启动应用