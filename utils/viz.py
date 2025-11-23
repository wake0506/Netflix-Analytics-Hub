import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

# --- Design System ---
COLOR_SCALE = px.colors.qualitative.Bold
SEQ_COLOR = px.colors.sequential.Viridis
TEMPLATE = "plotly_white"

# --- 1. KPI & Overview Charts ---

def plot_kpi_cards(total, movies, tv):
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Titles", f"{total:,}")
    col2.metric("Movies", f"{movies:,}")
    col3.metric("TV Shows", f"{tv:,}")

def plot_type_donut(df):
    """Chart 1: Donut Chart of Type Distribution"""
    counts = df['type'].value_counts().reset_index()
    counts.columns = ['type', 'count']
    fig = px.pie(counts, values='count', names='type', hole=0.6,
                 title='Content Distribution',
                 color_discrete_sequence=COLOR_SCALE, template=TEMPLATE)
    return fig

def plot_added_area(df):
    """Chart 2: Area Chart of Added Content Over Time"""
    data = df.groupby(['added_year', 'type']).size().reset_index(name='count')
    fig = px.area(data, x='added_year', y='count', color='type',
                  title='Growth of Content Library',
                  color_discrete_sequence=COLOR_SCALE, template=TEMPLATE)
    fig.update_layout(xaxis_title="Year Added", yaxis_title="Titles Added")
    return fig

def plot_release_line(df):
    """Chart 3: Line Chart of Release Years"""
    data = df.groupby(['release_year', 'type']).size().reset_index(name='count')
    data = data[data['release_year'] > 1990] # Focus on modern era
    fig = px.line(data, x='release_year', y='count', color='type',
                  title='Original Release Year Trends (Post-1990)',
                  color_discrete_sequence=COLOR_SCALE, template=TEMPLATE)
    return fig

def plot_heatmap(df):
    """Chart 4: Heatmap of Month vs Year"""
    df_clean = df.dropna(subset=['added_year', 'added_month_num'])
    data = df_clean.groupby(['added_year', 'added_month_num']).size().reset_index(name='count')
    pivot = data.pivot(index='added_month_num', columns='added_year', values='count').fillna(0)
    
    fig = px.imshow(pivot, 
                    labels=dict(x="Year", y="Month", color="Count"),
                    y=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                    title='Content Addition Intensity Heatmap',
                    color_continuous_scale=SEQ_COLOR, template=TEMPLATE)
    return fig

# --- 2. Geography Charts ---

def plot_world_map(df):
    """Chart 5: Choropleth Map"""
    data = df['primary_country'].value_counts().reset_index()
    data.columns = ['country', 'count']
    data = data[data['country'] != 'Unknown']

    fig = px.choropleth(data, locations="country", locationmode='country names',
                        color="count", hover_name="country",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        title='Global Content Source Distribution',
                        template=TEMPLATE)
    fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
    return fig

def plot_top_countries_bar(df):
    """Chart 6: Horizontal Bar of Top Countries"""
    data = df['primary_country'].value_counts().head(10).reset_index()
    data.columns = ['country', 'count']
    data = data[data['country'] != 'Unknown']
    
    fig = px.bar(data, x='count', y='country', orientation='h',
                 title='Top 10 Producing Countries',
                 color='count', color_continuous_scale=SEQ_COLOR, template=TEMPLATE)
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    return fig

# --- 3. Duration Charts ---

def plot_movie_duration_hist(df):
    """Chart 7: Histogram of Movie Durations"""
    data = df[df['type'] == 'Movie'].dropna(subset=['duration_min'])
    fig = px.histogram(data, x='duration_min', nbins=50,
                       title='Distribution of Movie Lengths',
                       marginal='box',
                       color_discrete_sequence=[COLOR_SCALE[1]], template=TEMPLATE)
    fig.update_layout(xaxis_title="Minutes")
    return fig

def plot_tv_seasons_bar(df):
    """Chart 8: Bar Chart of TV Seasons"""
    data = df[df['type'] == 'TV Show'].dropna(subset=['seasons'])
    counts = data['seasons'].value_counts().reset_index()
    counts.columns = ['seasons', 'count']
    
    fig = px.bar(counts, x='seasons', y='count',
                 title='Longevity of TV Shows (Seasons)',
                 color_discrete_sequence=[COLOR_SCALE[2]], template=TEMPLATE)
    return fig

def plot_duration_scatter(df):
    """Chart 9: Scatter of Year vs Duration"""
    data = df[df['type'] == 'Movie'].dropna(subset=['duration_min', 'release_year'])
    if len(data) > 1000: data = data.sample(1000) # Sample for performance
    
    fig = px.scatter(data, x='release_year', y='duration_min',
                     title='Movie Duration vs Release Year',
                     opacity=0.6,
                     color_discrete_sequence=[COLOR_SCALE[3]], template=TEMPLATE)
    return fig

def plot_genre_duration_box(df):
    """Chart 10: Box Plot of Duration by Genre"""
    data = df[df['type'] == 'Movie'].dropna(subset=['duration_min', 'listed_in'])
    data['primary_genre'] = data['listed_in'].apply(lambda x: x.split(',')[0])
    
    top_genres = data['primary_genre'].value_counts().head(8).index
    data = data[data['primary_genre'].isin(top_genres)]
    
    fig = px.box(data, x='primary_genre', y='duration_min',
                 title='Duration Variance by Top Genres',
                 color='primary_genre', template=TEMPLATE)
    return fig

# --- 4. Content & Ratings Charts ---

def plot_genre_treemap(df):
    """Chart 11: Treemap of Genres"""
    genres = df['listed_in'].str.split(', ').explode().value_counts().head(20).reset_index()
    genres.columns = ['genre', 'count']
    
    fig = px.treemap(genres, path=['genre'], values='count',
                     title='Top 20 Genres Hierarchy',
                     color='count', color_continuous_scale=SEQ_COLOR, template=TEMPLATE)
    return fig

def plot_genre_bar(df):
    """Chart 12: Bar Chart of Genres"""
    genres = df['listed_in'].str.split(', ').explode().value_counts().head(10).reset_index()
    genres.columns = ['genre', 'count']
    
    fig = px.bar(genres, x='genre', y='count',
                 title='Top 10 Most Common Genres',
                 color_discrete_sequence=COLOR_SCALE, template=TEMPLATE)
    return fig

def plot_rating_bar(df):
    """Chart 13: Ratings Distribution"""
    counts = df['rating'].value_counts().reset_index()
    counts.columns = ['rating', 'count']
    
    fig = px.bar(counts, x='rating', y='count',
                 title='Content Rating Distribution',
                 color_discrete_sequence=[COLOR_SCALE[4]], template=TEMPLATE)
    fig.update_layout(xaxis={'categoryorder':'total descending'})
    return fig

def plot_rating_stack(df):
    """Chart 14: Ratings by Type Stacked"""
    counts = df.groupby(['rating', 'type']).size().reset_index(name='count')
    fig = px.bar(counts, x='rating', y='count', color='type',
                 title='Ratings Composition by Type',
                 barmode='stack',
                 color_discrete_sequence=COLOR_SCALE, template=TEMPLATE)
    fig.update_layout(xaxis={'categoryorder':'total descending'})
    return fig

def plot_directors_bar(df):
    """Chart 15: Top Directors"""
    data = df[df['director'] != 'Unknown']
    counts = data['director'].value_counts().head(10).reset_index()
    counts.columns = ['director', 'count']
    
    fig = px.bar(counts, x='count', y='director', orientation='h',
                 title='Top 10 Prolific Directors',
                 color_discrete_sequence=[COLOR_SCALE[5]], template=TEMPLATE)
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    return fig

def plot_added_day_bar(df):
    """Chart 16: Content Added by Day of Month"""
    data = df.dropna(subset=['added_day'])
    counts = data['added_day'].value_counts().sort_index().reset_index()
    counts.columns = ['day', 'count']
    
    fig = px.bar(counts, x='day', y='count',
                 title='Content Releases by Day of Month',
                 color_discrete_sequence=[COLOR_SCALE[0]], template=TEMPLATE)
    fig.update_layout(xaxis=dict(tickmode='linear', dtick=1))
    return fig