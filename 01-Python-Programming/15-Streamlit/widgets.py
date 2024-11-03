import streamlit as st
import pandas as pd

## Title of the application
st.title("Streamlit Text Input")

name = st.text_input("Enter your name: ")
age = st.slider("Select your age: ", 0, 100, 25)

choices = ['Python', 'Java', 'C++']
choice = st.selectbox("Choose your favourite Programming Language: ", options=choices)

if name:
    st.write(f"Hello: {name}")
    st.write(f"Your age is: {age}")
    st.write(f"Your Favourite Programming Language is: {choice}")


uploaded_file = st.file_uploader("Choose a CSV File", type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df.head())