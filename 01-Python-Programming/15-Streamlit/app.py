import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello Streamlit")

## Display a Simple Text
st.write("This is a Simple Text")

## Create a DataFrame
df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [1, 4, 9, 16]
})

## Display the DataFrame
st.write("Here is the Data Frame")
st.write(df)

## Create a Line Chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=['a', 'b','c']
)
st.line_chart(chart_data)