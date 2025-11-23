Netflix Content Strategy Analysis Hub

Project: Streamlit Data Story | Instructor: Mano Mathew | Student: Zhuoyang Xu

This is an interactive data analytics dashboard built using Python and Streamlit. Its purpose is to perform a deep-dive analysis into Netflix's content library, revealing the evolution of its content acquisition strategy, global expansion, and audience targeting.

Quick Start

This application is a Streamlit web app. You can have it up and running locally in just a few steps.

1. Environment Setup

Ensure you have Python 3.8 or higher installed. It is highly recommended to use a virtual environment (venv).

# 1. Clone the GitHub Repository
git clone [https://github.com/wake0506/Netflix-Analytics-Hub.git]
cd Netflix-Analytics-Hub

# 2. (Optional) Create and Activate Virtual Environment
python -m venv venv
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate


2. Install Dependencies

All necessary Python libraries are listed in the requirements.txt file (including streamlit, pandas, plotly, etc.).

pip install -r requirements.txt


3. Required Assets

Please ensure the following data and image files are present in the project's root directory (alongside app.py):

Ntitles.csv: The core dataset containing Netflix movies and TV shows details.

微信图片_20251121083856_35_777.png: Custom Logo 2 (Displayed in the sidebar).

retouch_2025112400100760.png: Custom Logo 1 (Displayed in the sidebar).

4. Run the Application

In your terminal, confirm you are in the project root directory and your virtual environment is active, then execute:

streamlit run app.py


The application will automatically open in your default web browser (typically at http://localhost:8501).

Dashboard Structure and Usage

The dashboard is organized into four main sections, accessible via the navigation radio buttons in the left sidebar.

1. Introduction

Content: Provides the executive summary, strategic context, key analysis objectives, and a data dictionary/health check of the Ntitles.csv dataset.

Interaction: This is a static overview page.

2. Macro Overview

Content: Focuses on high-level trends, including content library growth over time and the composition of content (Movies vs. TV Shows).

Key Visualizations: Area Charts for content growth, Donut Chart for type distribution, and a Heatmap illustrating content acquisition seasonality by month and year.

3. Deep Dive Analysis

This is the core interactive analysis, segmented into four tabs:

Geography (Global Strategy)

Detailed Analysis: Features a Choropleth Map of primary content countries and a bar chart of the Top 10 Producing Countries, highlighting Netflix's global expansion focus.

Duration & Operations (Content Format Metrics)

Detailed Analysis: Includes Histograms for Movie durations, bar charts for TV Show seasons, scatter plots of release year vs. duration, and analysis of content release day patterns.

Genres (Thematic Composition)

Detailed Analysis: Visualizations like Treemaps and bar charts are used to show the popularity and hierarchy of the most common content genres.

Talent & Ratings (Audience & Creators)

Detailed Analysis: Features bar charts displaying Content Rating distributions (e.g., TV-MA, PG-13) and a ranked list of the Top 10 most prolific Directors.

4. Conclusions

Content: Offers a synthesized strategic conclusion based on data insights, discusses the limitations of the dataset, and provides actionable recommendations for future content investment.

Sidebar Filters

The left sidebar includes essential global filters (available in the Macro Overview and Deep Dive Analysis sections) to refine the data used in all charts.

Content Type: Filters titles to show only Movie or TV Show, or both. Example Use Case: Analyze only the growth trends of TV series.

Date Added Range: Filters based on the year the content was added to the platform. Example Use Case: Focus analysis on content added since 2018 to see recent trends.

Primary Country: Filters titles whose production country matches any of the selected options. Example Use Case: Compare content characteristics exclusively from the United States and India.

Project Structure

Netflix-Analytics-Hub/
├── app.py                  # Main Streamlit application entry point.
├── Ntitles.csv             # Primary data file.
├── requirements.txt        # List of Python dependencies.
├── .gitignore              # Files ignored by Git.
├── utils/                  # Utility functions for data handling.
│   ├── io.py               # Data loading and Streamlit caching.
│   ├── prep.py             # Data cleaning, feature engineering, and filtering.
│   └── viz.py              # Plotly chart generation functions.
└── sections/               # Modularized content for each dashboard page.
    ├── intro.py            # Introduction page logic.
    ├── overview.py         # Macro Overview page logic.
    ├── deep_dives.py       # Deep Dive Analysis page logic.
    └── conclusions.py      # Conclusions page logic.


Contributor Information

Prof: Mano Mathew

My name: Zhuoyang Xu

Github: wake0506/Netflix-Analytics-Hub.git