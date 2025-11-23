import streamlit as st
from utils import viz

def show(df):
    st.markdown("## 🕵️‍♂️ Deep Dive Analysis")
    st.write("Granular breakdown by Geography, Duration, Content DNA, and Production.")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🌍 Geography", "⏱️ Duration & Operations", "🎭 Genres", "👥 Talent & Ratings"])
    
    # --- Tab 1: Geography ---
    with tab1:
        st.subheader("Global Content Footprint")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.plotly_chart(viz.plot_world_map(df), use_container_width=True)
        with col2:
            st.plotly_chart(viz.plot_top_countries_bar(df), use_container_width=True)
        
        st.markdown("**Globalization Strategy**: While the US dominates, significant clusters in India, UK, and South Korea highlight a 'Local-for-Global' acquisition strategy.")

    # --- Tab 2: Duration ---
    with tab2:
        st.subheader("Technical Characteristics")
        
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(viz.plot_movie_duration_hist(df), use_container_width=True)
        with col2:
            st.plotly_chart(viz.plot_tv_seasons_bar(df), use_container_width=True)
            
        col3, col4 = st.columns(2)
        with col3:
            st.plotly_chart(viz.plot_duration_scatter(df), use_container_width=True)
        with col4:
            st.plotly_chart(viz.plot_genre_duration_box(df), use_container_width=True)
            
        st.caption("Release Logic: We also analyzed on which day of the month content drops.")
        st.plotly_chart(viz.plot_added_day_bar(df), use_container_width=True)
        st.info("💡 **Insight**: There is a massive spike on the 1st of the month, indicating a batch-release operational model for licensed content.")

    # --- Tab 3: Genres ---
    with tab3:
        st.subheader("Thematic Composition")
        st.plotly_chart(viz.plot_genre_treemap(df), use_container_width=True)
        st.plotly_chart(viz.plot_genre_bar(df), use_container_width=True)

    # --- Tab 4: Talent & Ratings ---
    with tab4:
        st.subheader("Audience & Creators")
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(viz.plot_rating_bar(df), use_container_width=True)
        with col2:
            st.plotly_chart(viz.plot_rating_stack(df), use_container_width=True)
            
        st.divider()
        st.plotly_chart(viz.plot_directors_bar(df), use_container_width=True)