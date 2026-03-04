import streamlit as st
import pandas as pd

st.sidebar.radio(
    'Select',
    ('Medals-Wise','Overall','Country-Wise','Athlete-Wise')
)
st.header("Olympics")