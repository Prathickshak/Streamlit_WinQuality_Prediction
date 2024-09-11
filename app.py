import streamlit as st
from explore_page import show_explore_page
from predict_page import show_predicted_page

page = st.sidebar.selectbox("Data About Wine Qualities Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predicted_page()
else:
    show_explore_page()