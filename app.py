import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np



## STREAMLIT
#TEXT
#DATA (TABLES)
# st.table()
# st.dataframe()
# #GRAPHS
# st.plotly_chart()
# st.pyplot()

df = px.data.iris()

## WIDGETS
# selectbox
# date picker
# radio button

st.sidebar.write('My sidebar')
selection = st.sidebar.selectbox('Pick an option:', ['Option1', 'Option2', 'option3'])

if selection == 'Option1':
    fig = px.scatter(df, x='petal_length', y='petal_width', color='species')
    st.plotly_chart(fig)
elif selection == 'Option2':
    fig = px.scatter(df, x='sepal_length', y='petal_width', color='species')
    st.plotly_chart(fig)
else:
    fig = px.scatter(df, x='petal_length', y='sepal_width', color='species')
    st.plotly_chart(fig)

## LAYOUT

col1, col2, colt = st.columns(3)

with col1:
    st.write('My first column')
    fig = px.scatter(df, x='petal_length', y='petal_width', color='species')
    st.plotly_chart(fig)
with col2:
    st.write('My second column')
    fig = px.scatter(df, x='sepal_length', y='sepal_width', color='species')
    st.plotly_chart(fig)
with colt:
    st.write('My thrird third column')
    fig = px.scatter(df, x='sepal_length', y='sepal_width', color='species')
    st.plotly_chart(fig)

col3, col4 = st.columns(2)

with col3:
    st.write('My third column')
    fig = px.scatter(df, x='petal_length', y='petal_width', color='species')
    st.plotly_chart(fig)
with col4:
    st.write('My fourth column')
    fig = px.scatter(df, x='sepal_length', y='sepal_width', color='species')
    st.plotly_chart(fig)






# st.write('Paragraph 1')
# st.title('New title')

# ctr + s