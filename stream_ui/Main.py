import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px 
import base64
st.set_page_config(page_title='Jobs Page', page_icon='🏠')

with open('img.jpg', 'rb') as f:
    file= f.read()
img =  base64.b64encode(file).decode()

css=f"""
    <style>
    [data-testid="stAppViewContainer"]{{
        background-image:url('data:image/png;base64,{img}');
        background-size:cover
    }}
    </style>
"""

st.markdown(css, unsafe_allow_html=True)

df= pd.read_csv('AI_Impact_on_Jobs_2030.csv')
# st.dataframe(df)
st.write(df)
# st.table(df)

# st.write(df.Job_Title.value_counts())
st.subheader("Pie chart of Salary according to Job Title")
ch1= px.pie(names=df.Job_Title.value_counts().index, values=df.Job_Title.value_counts().values)
st.plotly_chart(ch1)

