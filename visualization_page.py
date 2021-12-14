import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import plotly.offline as pyo
import seaborn as sns

@st.cache
def load_data():
    df = pd.read_csv("BankChurnersV2.csv")
    df['Customer_Age'] = df['Customer_Age'].fillna(df['Customer_Age'].mode()[0])
    df['Credit_Limit'] = df['Credit_Limit'].fillna(df['Credit_Limit'].mode()[0])
    df['Avg_Open_To_Buy'] = df['Avg_Open_To_Buy'].fillna(df['Avg_Open_To_Buy'].mode()[0])
    return df

df = load_data()

def show_visualization_page():
    st.title("Explore Bank's Customers Data")
    
    # Distribution of Customers Age
    fig = make_subplots(rows=2, cols=1)
    tr1=go.Box(x=df['Customer_Age'],name='Age Box Plot',boxmean=True)
    tr2=go.Histogram(x=df['Customer_Age'],name='Age Histogram')
    fig.add_trace(tr1,row=1,col=1)
    fig.add_trace(tr2,row=2,col=1)
    fig.update_layout(height=700, width=900)
    
    st.write("""### Distribution of Customer Age""")
    st.plotly_chart(fig, use_container_width=True)
    
    # Proportion of Gender
    st.write("""### Proportion of Gender""")
    fig2 = px.pie(df, names='Gender')
    st.plotly_chart(fig2,use_container_width=True)
    
    # Distribution of Dependant counts
    fig3 = make_subplots(rows=2, cols=1)

    tr1=go.Box(x=df['Dependent_count'],name='Dependant count Box Plot',boxmean=True)
    tr2=go.Histogram(x=df['Dependent_count'],name='Dependant count Histogram')

    fig3.add_trace(tr1,row=1,col=1)
    fig3.add_trace(tr2,row=2,col=1)

    fig3.update_layout(height=700, width=900)
    st.write("""### Distribution of Dependant counts""")
    st.plotly_chart(fig, use_container_width=True)
    
    # Customers' Education Level
    fig4 = plt.figure(figsize=(13,4),dpi=200)
    sns.countplot(x='Education_Level',data=df,palette='Set1')
    st.write("""### Customers' Education Level""")
    st.pyplot(fig4)
    
    # Proportion of Marriage Statuses
    fig5 = px.pie(df,names='Marital_Status',hole=0.4)
    st.write("""### Proportion of Marriage Statuses""")
    st.plotly_chart(fig5, use_container_width=True)
    
    # Customers' Income Category
    fig6 = plt.figure(figsize=(10,4),dpi=200)
    sns.countplot(x='Income_Category',data=df,palette='Set1')
    st.write("""### Customers' Income Category""")
    st.pyplot(fig6)
    
    #Proportion 0f Card Category
    fig7 = px.pie(df,names='Card_Category')
    st.write("""### Proportion of Card Category""")
    st.plotly_chart(fig7, use_container_width=True)
    
    # Distribution of the Number of Months the Customer use Bank services
    fig8 = make_subplots(rows=2, cols=1)

    tr1=go.Box(x=df['Months_on_book'],name='Box Plot',boxmean=True)
    tr2=go.Histogram(x=df['Months_on_book'],name='Histogram')

    fig8.add_trace(tr1,row=1,col=1)
    fig8.add_trace(tr2,row=2,col=1)

    fig8.update_layout(height=700, width=1000)
    st.write("""### Distribution of the Number of Months the Customer use Bank services""")
    st.plotly_chart(fig8, use_container_width=True)
    
    # Distribution of Credit LImit
    fig9 = make_subplots(rows=2, cols=1)

    tr1=go.Box(x=df['Credit_Limit'],name='Credit_Limit Box Plot',boxmean=True)
    tr2=go.Histogram(x=df['Credit_Limit'],name='Credit_Limit Histogram')

    fig9.add_trace(tr1,row=1,col=1)
    fig9.add_trace(tr2,row=2,col=1)

    fig9.update_layout(height=700, width=1000)
    st.write("""### Distribution of the Credit Limit""")
    st.plotly_chart(fig9, use_container_width=True)
    
    # Proportion of Churn vs Not Churn Customers
    fig10 = px.pie(df,names='Attrition_Flag', hole=0.43)
    st.write("""### Proportion of Churn vs Not Churn Customers""")
    st.plotly_chart(fig10, use_container_width=True)