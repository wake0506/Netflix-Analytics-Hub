import streamlit as st
import pandas as pd

def show(df):
    st.markdown("## 📖 Executive Summary & Data Scope")
    
    st.markdown("""
    > **Strategic Context**: In the rapidly evolving streaming landscape, understanding content acquisition patterns is crucial. This dashboard analyzes over 8,000 titles to decode the platform's shift from licensed movies to original series and its global expansion strategy.
    
    **Key Objectives:**
    1.  **Analyze** the temporal shift in content type (Movies vs. TV Shows).
    2.  **Map** the global footprint of production sources.
    3.  **Evaluate** audience targeting strategies through ratings and duration metrics.
    """)
    
    st.divider()
    
    st.subheader("🔍 Data Quality & Composition")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**Dataset Preview:**")
        st.dataframe(df.head(5), use_container_width=True)
    
    with col2:
        st.markdown("**Data Health Check:**")
        missing = df.isnull().sum()
        missing = missing[missing > 0]
        if not missing.empty:
            st.warning("Missing Fields Detected:")
            st.bar_chart(missing)
            st.caption("Categorical fields filled with 'Unknown'. Dates coerced.")
        else:
            st.success("Dataset is pristine.")
            
    with st.expander("Show Data Dictionary"):
        st.markdown("""
        - **show_id**: Unique ID for every Movie / TV Show
        - **type**: Identifier - A Movie or TV Show
        - **title**: Title of the Movie / TV Show
        - **director**: Director of the Movie
        - **cast**: Actors involved in the movie / show
        - **country**: Country where the movie / show was produced
        - **date_added**: Date it was added on Netflix
        - **release_year**: Actual Release year of the move / show
        - **rating**: TV Rating of the movie / show
        - **duration**: Total Duration - in minutes or number of seasons
        """)