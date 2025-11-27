import streamlit as st
import requests

st.set_page_config(page_title="Number Facts", page_icon="🔢")

st.markdown("# 🔢 Number Facts")
st.sidebar.header("Number Facts")
st.write(
    """This page fetches fun facts about numbers using the [Numbers API](http://numbersapi.com/)."""
)

number = st.number_input("Enter a number", value=42, step=1)

if st.button("Get Fact"):
    try:
        response = requests.get(f"http://numbersapi.com/{number}")
        if response.status_code == 200:
            st.success(response.text)
        else:
            st.error("Failed to fetch fact. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
