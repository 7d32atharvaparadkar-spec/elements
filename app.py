import streamlit as st
import pandas as pd

# Load CSV safely
try:
    df = pd.read_csv("elements.csv")
except:
    st.error("❌ elements.csv file not found")
    st.stop()

# Title
st.title("⚛️ Element Type Finder")
st.write("Find whether an element is Metal, Non-metal or Metalloid")

# Input
element = st.text_input("Enter Element Name")

# Button
if st.button("Find Type"):
    
    if element.strip() == "":
        st.warning("⚠️ Please enter an element name")
    
    else:
        element = element.capitalize()
        result = df[df["Element"] == element]

        if not result.empty:
            st.success(f"✅ {element} is a **{result['Type'].values[0]}**")
        else:
            st.error("❌ Element not found in database")

# Show dataset (optional)
if st.checkbox("Show All Elements"):
    st.dataframe(df)