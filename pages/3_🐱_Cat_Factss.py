import streamlit as st
import requests

st.set_page_config(page_title="Cat Facts", page_icon="🐱")

st.markdown("# 🐱 Cat Facts")
st.sidebar.header("Cat Facts")
st.write(
    """This page fetches a random cat fact from the [Cat Fact API](https://catfact.ninja/)."""
)

if st.button("Get Cat Fact"):
    try:
        response = requests.get("https://catfact.ninja/fact")
        if response.status_code == 200:
            data = response.json()
            st.info(data["fact"])
        else:
            st.error("Failed to fetch cat fact. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
