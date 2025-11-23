import streamlit as st
import pandas as pd
import os

# 1. Page Config (Must be the first command)
st.set_page_config(
    page_title="Netflix Analytics Hub",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Imports
from utils import io, prep
from sections import intro, overview, deep_dives, conclusions

# 3. Constants
DATA_PATH = 'Ntitles.csv'
LOGO_2 = '微信图片_20251121083856_35_777.png'
LOGO_1 = 'retouch_2025112400100760.png'

def main():
    # --- Sidebar UI ---
    
    # 调整 Logo 布局：两个 Logo 并排放在侧边栏顶部
    st.sidebar.markdown("""
        <style>
            .sidebar-logo-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 1.5rem;
            }
            .sidebar-logo-container img {
                max-width: 48%; /* Ensure both images fit side-by-side */
            }
        </style>
    """, unsafe_allow_html=True)
    
    # 使用自定义 HTML/Markdown 容器实现并排布局
    st.sidebar.markdown('<div class="sidebar-logo-container">', unsafe_allow_html=True)
    
    # Logo 1
    if os.path.exists(LOGO_1):
        st.sidebar.image(LOGO_1)
    
    # Logo 2
    if os.path.exists(LOGO_2):
        st.sidebar.image(LOGO_2)

    st.sidebar.markdown('</div>', unsafe_allow_html=True)
    
    st.sidebar.title("Netflix Analytics")
    st.sidebar.caption("Strategic Content Intelligence")
    st.sidebar.markdown("---")
    
    # Navigation
    page = st.sidebar.radio(
        "Navigate", 
        ["Introduction", "Macro Overview", "Deep Dive Analysis", "Conclusions"],
        index=0
    )
    
    # --- Data Loading ---
    raw_df = io.load_data(DATA_PATH)
    
    if raw_df.empty:
        st.stop()
        
    df = prep.clean_data(raw_df)
    
    # --- Global Filter Logic ---
    # We hide filters on the Intro page to keep it clean
    if page != "Introduction":
        st.sidebar.markdown("---")
        st.sidebar.subheader("🛠️ Filters")
        
        # Filter 1: Type
        all_types = df['type'].unique().tolist()
        selected_types = st.sidebar.multiselect("Content Type", all_types, default=all_types)
        
        # Filter 2: Year Range
        valid_years = df['added_year'].dropna()
        if not valid_years.empty:
            min_year = int(valid_years.min())
            max_year = int(valid_years.max())
            default_start = 2015 if 2015 > min_year else min_year
            
            selected_years = st.sidebar.slider(
                "Date Added Range",
                min_year, max_year, (default_start, max_year)
            )
        else:
            selected_years = None
            
        # Filter 3: Country
        # Get unique countries, exclude Unknown, sort
        all_countries = sorted(list(set([c for c in df['primary_country'].unique() if c and c != 'Unknown'])))
        selected_countries = st.sidebar.multiselect("Primary Country", all_countries)
        
        # Apply Filters
        filtered_df = prep.filter_data(df, selected_types, selected_years, selected_countries)
        
        # Show metric
        st.sidebar.info(f"Showing: {len(filtered_df)} titles")
    else:
        filtered_df = df

    # --- Student Info at the BOTTOM of Sidebar ---
    # Adding some spacing to push it down visually if content is short
    st.sidebar.markdown("---")
    st.sidebar.markdown("<br>", unsafe_allow_html=True) 
    
    # 添加作者信息和Github链接 (Add Author Info and Github Link)
    st.sidebar.markdown(f"""
        **Prof: Mano Mathew**
        
        **My name: Zhuoyang Xu**
        
        **Github:** [wake0506/Netflix-Analytics-Hub.git](https://github.com/wake0506/Netflix-Analytics-Hub.git)
    """)
    

    # --- Page Routing ---
    st.title("Netflix Content Strategy Report")
    
    if page == "Introduction":
        intro.show(df)
    elif page == "Macro Overview":
        overview.show(filtered_df)
    elif page == "Deep Dive Analysis":
        deep_dives.show(filtered_df)
    elif page == "Conclusions":
        conclusions.show()

if __name__ == "__main__":
    main()