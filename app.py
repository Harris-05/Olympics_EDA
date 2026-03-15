import streamlit as st
import pandas as pd
import preprocess, helper
import numpy as np


df = preprocess.preprocess()

user_menu = st.sidebar.radio(
    'Select',
    ('Medals-Wise', 'Overall', 'Country-Wise')
)

st.header("Olympics")

years = df['Year'].unique().tolist()
years.sort()
years.insert(0, 'Overall')

region = df['region'].dropna().unique().tolist()
region.sort() 
region.insert(0, 'Overall')

if user_menu == "Medals-Wise":
  
    df = df.sort_values('ID', ascending=True).reset_index(drop=True)
    st.dataframe(df)
    
    st.sidebar.header("Medal Wise")
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_region = st.sidebar.selectbox("Select Country", region)
    
    medal_tally = helper.medal_tally(df, selected_year, selected_region)
    
    if selected_year == 'Overall' and selected_region == 'Overall':
        st.title("Overall Tally")
    if selected_year == 'Overall' and selected_region != 'Overall':
        st.title(f"Country Wise in Country: {selected_region}")
    if selected_year != 'Overall' and selected_region == 'Overall':
        st.title(f"Year Wise in year: {selected_year}")
    if selected_year != 'Overall' and selected_region != 'Overall':
        st.title(f"Country in: {selected_region} in Year: {selected_year}")
        
    st.dataframe(medal_tally)

if user_menu == 'Overall':
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

if user_menu == 'Country-Wise':
    st.title("Country Wise Analysis")
    region.remove('Overall')
    country = st.sidebar.selectbox("Select A Country", region)
    
    st.title(f"{country} Medal Tally Over the Years")
    
    country_df = helper.yearwise_medal(df, country)
    st.dataframe(country_df)
    top_df = helper.most_successful(df, country=country)
    
    st.title(f"Top 10 Athletes from {country}") 
    st.table(top_df)