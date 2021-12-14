import streamlit as st
import pickle
import numpy as np

def show_predict_page():
    st.title("Customer Churn Prediction")
    
    st.write("""### Fill in the customer informations""")