import streamlit as st
import requests

st.set_page_config(page_title="Cat Facts", page_icon="🐱")

st.markdown("# 🐱 Daily Cat Facts")
st.sidebar.header("Cat Facts")
st.write("Get a random interesting fact about cats!")

if st.button("🐱 Get New Fact"):
    try:
        response = requests.get("https://cat-fact.herokuapp.com/facts/random?amount=1")
        if response.status_code == 200:
            data = response.json()
            fact = data.get("text", "No fact found.")
            st.info(f"**Did you know?** {fact}")
        else:
            st.error("Could not fetch cat fact.")
    except Exception as e:
        st.error(f"Error: {e}")
