import pandas as pd
import numpy as np

def clean_data(df):
    """
    Performs data cleaning, standardization, and feature engineering.
    """
    if df.empty:
        return df
        
    df = df.copy()
    
    # 1. Handle Missing Values
    # Fill categorical missing values
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    df['country'] = df['country'].fillna('Unknown')
    df['rating'] = df['rating'].fillna('Unknown')
    
    # 2. Handle Dates
    # Coerce errors to handle dirty date formats
    df['date_added'] = df['date_added'].astype(str).str.strip()
    df['date_added_dt'] = pd.to_datetime(df['date_added'], errors='coerce')
    
    # Extract temporal features
    df['added_year'] = df['date_added_dt'].dt.year
    df['added_month'] = df['date_added_dt'].dt.month_name()
    df['added_month_num'] = df['date_added_dt'].dt.month
    df['added_day'] = df['date_added_dt'].dt.day
    
    # 3. Handle Duration
    if 'duration' in df.columns:
        temp_duration = df['duration'].astype(str)
        # Extract minutes for movies (e.g., "90 min")
        df['duration_min'] = temp_duration.str.extract(r'(\d+)\s*min')[0].astype(float)
        # Extract season count for TV Shows (e.g., "2 Seasons")
        df['seasons'] = temp_duration.str.extract(r'(\d+)\s*Season')[0].astype(float)
    else:
        df['duration_min'] = np.nan
        df['seasons'] = np.nan
    
    # 4. Handle Countries
    # Many titles have multiple countries; we take the first one as "Primary Country"
    if 'country' in df.columns:
        df['primary_country'] = df['country'].apply(
            lambda x: x.split(',')[0].strip() if isinstance(x, str) and x else 'Unknown'
        )
    else:
        df['primary_country'] = 'Unknown'

    # 5. Split Genres (create a list for analysis later)
    df['genre_list'] = df['listed_in'].astype(str).str.split(', ')

    return df

def filter_data(df, selected_types, selected_years, selected_countries):
    """
    Filters the dataframe based on sidebar inputs.
    """
    temp_df = df.copy()
    
    # Filter by Type
    if selected_types:
        temp_df = temp_df[temp_df['type'].isin(selected_types)]
        
    # Filter by Year
    if selected_years and 'added_year' in temp_df.columns:
        min_year, max_year = selected_years
        temp_df = temp_df[
            (temp_df['added_year'] >= min_year) & 
            (temp_df['added_year'] <= max_year)
        ]
        
    # Filter by Country
    if selected_countries:
        # Check if the row's country string contains ANY of the selected countries
        mask = temp_df['country'].apply(lambda x: any(c in x for c in selected_countries) if isinstance(x, str) else False)
        temp_df = temp_df[mask]
        
    return temp_df