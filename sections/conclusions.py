import streamlit as st

def show():
    st.markdown("## 📝 Strategic Conclusions")
    
    st.success("### Executive Summary")
    st.markdown("""
    1.  **Pivot to Originals**: The platform has successfully transitioned from a movie aggregator to a series-first network, evidenced by the rising share of TV Shows and multi-season renewals.
    2.  **Global Diversification**: The dependency on Hollywood has decreased, with robust content pipelines established in **India, the UK, and East Asia**.
    3.  **Audience Maturity**: The dominance of **TV-MA** and **TV-14** ratings suggests a clear focus on retaining adult households rather than competing directly with niche children's platforms.
    4.  **Operational Cadence**: The **1st-of-month spike** suggests a legacy licensing model is still active alongside the more fluid release schedule of Originals.
    """)
    
    st.warning("### Data Limitations")
    st.markdown("""
    * **Temporal Cutoff**: Dataset concludes in 2021; recent ad-tier impacts are excluded.
    * **Performance Blindspot**: Analysis is based on *volume*, not *viewership*. A title's presence does not equate to its success.
    """)
    
    st.info("### Recommendations")
    st.markdown("""
    * **Invest in Regional Content**: Doubling down on South Korean and Spanish production hubs has yielded high volume; continue this 'Local-Global' bridge.
    * **Monitor Duration Drift**: Movie runtimes are stable, but 'Limited Series' are blurring the lines between formats.
    * **Data Integration**: Incorporate IMDB/Rotten Tomatoes scores to correlate content volume with quality reception.
    """)