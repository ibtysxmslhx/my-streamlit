import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#st.image(r'C:\Users\Userx\1AA DATA ANALYTIC\koko.jpeg')
st.image('ll.jpeg')

st.date_input("Select a date")

st.title("""Welcome to my Dashboard
This is my first time using streamlit.""")

#upload data
# Upload CSV file
upload_file = st.file_uploader("Please upload your CSV file here:", type='csv')

if upload_file is not None:
    df = pd.read_csv(upload_file)

#show data
st.subheader("Raw Data")
st.write(df)

#histogram
st.subheader("Histogram")
column = st.selectbox("Choose a column",df.columns) #boleh pilih y-axis nak yg mana2
fig, ax = plt.subplots(figsize = (10,6))
df[column].plot(kind = 'hist', ax =ax)

st.pyplot(fig)
fig = px.histogram(df, x=column)
fig.update_traces( marker = {"color":"purple", "line":{"color":"black","width":2}})
st.plotly_chart(fig)

#Scatter chart
st.subheader("Scatter Chart")
x_column = st.selectbox("Choose x-axis column",df.columns)
y_column = st.selectbox("Choose y-axis column",df.columns)
fig, ax = plt.subplots(figsize = (10,6))
df.plot(kind = 'scatter', x=x_column, y=y_column, ax =ax)
st.pyplot(fig)

fig = px.scatter(df, x=x_column, y = y_column,color ='sex' , color_discrete_sequence= ['yellow', 'red'])
st.plotly_chart(fig)

