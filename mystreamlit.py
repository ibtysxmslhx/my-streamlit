import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Display image
st.image('ll.jpeg')

st.date_input("Select a date")

st.title("""Welcome to my Dashboard
This is my first time using streamlit.""")

# Load CSV from the same folder (auto-loads on app start)
df = pd.read_csv("Tips.csv")

    # Show data
    st.subheader("Raw Data")
    st.write(df)

    # Histogram
    st.subheader("Histogram")
    column = st.selectbox("Choose a column", df.columns)
    fig, ax = plt.subplots(figsize=(10, 6))
    df[column].plot(kind='hist', ax=ax)
    st.pyplot(fig)

    fig2 = px.histogram(df, x=column)
    fig2.update_traces(marker={"color": "purple", "line": {"color": "black", "width": 2}})
    st.plotly_chart(fig2)

    # Scatter chart
    st.subheader("Scatter Chart")
    x_column = st.selectbox("Choose x-axis column", df.columns, key='x_col')
    y_column = st.selectbox("Choose y-axis column", df.columns, key='y_col')
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    df.plot(kind='scatter', x=x_column, y=y_column, ax=ax3)
    st.pyplot(fig3)

    fig4 = px.scatter(df, x=x_column, y=y_column, color='sex', color_discrete_sequence=['yellow', 'red'])
    st.plotly_chart(fig4)

else:
    st.info("Please upload a CSV file to get started.")


