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
    st.title("Churnzy")
    st.text("""Predict your customer loyalty as fast as possible""")
    
    st.write("""#### Fill in the customer informations""")
    
    #Gender
    gender = ("M", "F")
    gender = st.selectbox("Select gender:", gender, help='M for Male and F for Female')
    #Age
    age = st.slider("Enter age:", min_value=21, max_value=100)
    # Total Transaction Count
    Total_Trans_Ct = st.number_input("Enter the total transaction count in last 12 months:", value=10, step=10, help='The total of transactions made for the last 12 months')
    # Total_Revolving_Bal
    Total_Revolving_Bal = st.number_input("Enter the total revolving balance on the credit card:", step=10, help='The revolving credit card balance')
    # Total_Trans_Amt
    Total_Trans_Amt = st.number_input("Enter the total transaction amount in last 12 months:", value=700, step=10, help='The total transaction amount made for the last 12 months')
    # Total_Relationship_Count
    Total_Relationship_Count = st.number_input("Enter the total number of products held by the customer:", 1, 6, step=1)
    
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
            
        
        
        