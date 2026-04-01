import streamlit as st
import pandas as pd

df = pd.read_csv("elements.csv")

st.title("⚛️ Element Type Finder")

element = st.text_input("Enter Element Name").capitalize()

if st.button("Find"):
    
    result = df[df["Element"] == element]
    
    if not result.empty:
        st.success(f"Type: {result['Type'].values[0]}")
    else:
        st.error("Element not found")