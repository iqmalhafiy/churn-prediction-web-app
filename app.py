import streamlit as st
from predict_page import show_predict_page
from visualization_page import show_visualization_page



page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_visualization_page()

userguide = '[User Guide](https://docs.google.com/document/d/1aGkYQK2eoN_S3ZZ8LNSHj-YXn1-2MAASmOmL5FV1UYQ/edit?usp=sharing)'
st.sidebar.text("For user guideline visit:")
st.sidebar.markdown(userguide)