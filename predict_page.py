import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

xgb = data["model"]
le_gender = data["le_gender"]
scaler = data["scaler"]

def show_predict_page():
    st.title("Customer Churn Prediction")
    
    st.subheader(""" Fill in the customer informations""")
    
    #Gender
    gender = ("M", "F")
    gender = st.selectbox("Select gender: (M = Male and F = Female)", gender)
    #Age
    age = st.slider("Enter age:", min_value=18, max_value=100, value=18)
    # Total Transaction Count
    Total_Trans_Ct = st.number_input("Enter total transaction count in last 12 months:", step=1)
    # Total_Revolving_Bal
    Total_Revolving_Bal = st.number_input("Enter the total revolving balance on the credit card:", step=1)
    # Total_Trans_Amt
    Total_Trans_Amt = st.number_input("Enter the total transaction amount in last 12 months:", step=1)
    # Total_Relationship_Count
    Total_Relationship_Count = st.number_input("Enter the total number of products held by the customer:", step=1)
    
    ok = st.button("Predict")
    if ok:
        X = np.array([[gender, age, Total_Trans_Ct, Total_Revolving_Bal, Total_Trans_Amt, Total_Relationship_Count]])
        X[:, 0] = le_gender.transform(X[:,0])
        X = scaler.transform(X)

        attrition_flag = xgb.predict(X)
        if (attrition_flag == 1):
            st.subheader(f"The customer is predicted to CHURN.")
        else:
            st.subheader(f"The customer is predicted to STAY.")
        
        