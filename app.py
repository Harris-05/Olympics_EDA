import streamlit as st
import pandas as pd
import preprocess,helper
import numpy as np
df=preprocess.preprocess()
user_menu=st.sidebar.radio(
    'Select',
    ('Medals-Wise','Overall','Country-Wise','Athlete-Wise')
)

st.header("Olympics")
st.dataframe(df)

years=df['Year'].unique().tolist()
years.sort()
years.insert(0,'Overall')
region = df['region'].dropna().unique().tolist()
region.sort() 
region.insert(0, 'Overall')

if user_menu == "Medals-Wise":
    st.sidebar.header("Medal Wise")
    selected_year=st.sidebar.selectbox("Select Year",years)
    selected_region=st.sidebar.selectbox("Select Country",region)
    medal_tally=helper.medal_tally(df,selected_year ,selected_region)
    if selected_year=='Overall' and selected_region=='Overall':
        st.title("Overall Tally")
    if selected_year=='Overall' and selected_region!='Overall':
        st.title("Country Wise in Country: "+selected_region)
    if selected_year!='Overall' and selected_region=='Overall':
        st.title("Year Wise in year: "+ selected_year)
    if selected_year!='Overall' and selected_region!='Overall':
        st.title("Country in : "+selected_region+ "in Year: "+str(selected_year))
    st.dataframe(medal_tally)




