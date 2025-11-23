import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_data(filepath):
    """
    Load CSV data with caching.
    """
    if not os.path.exists(filepath):
        st.error(f"File not found: {filepath}. Please upload 'Ntitles.csv' to the root directory.")
        return pd.DataFrame()
    
    try:
        df = pd.read_csv(filepath)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()