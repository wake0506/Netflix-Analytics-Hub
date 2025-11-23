import streamlit as st
from utils import viz

def show(df):
    st.markdown("## 📈 Macro Trends: Growth & Velocity")
    st.write("High-level metrics indicating platform scale and acquisition velocity.")
    
    # KPI Section
    total = len(df)
    movies = len(df[df['type'] == 'Movie'])
    tv = len(df[df['type'] == 'TV Show'])
    viz.plot_kpi_cards(total, movies, tv)
    
    st.divider()
    
    # Row 1: Composition and Growth
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(viz.plot_type_donut(df), use_container_width=True)
    with col2:
        st.plotly_chart(viz.plot_added_area(df), use_container_width=True)
        
    st.info("💡 **Insight**: The catalog has seen exponential growth post-2015. While movies constitute the majority, the acceleration of TV Show acquisitions signifies a strategic pivot toward retention-focused serial content.")

    # Row 2: Release Trends and Seasonality
    col3, col4 = st.columns(2)
    with col3:
        st.plotly_chart(viz.plot_release_line(df), use_container_width=True)
    with col4:
        st.plotly_chart(viz.plot_heatmap(df), use_container_width=True)
        
    st.markdown("**Operational Insight**: The heatmap reveals a strong Q4 (October-December) bias in content releases, likely aligning with holiday viewership spikes and awards season eligibility.")