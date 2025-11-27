import streamlit as st
import requests

st.set_page_config(page_title="Yo Momma", page_icon="👩")

st.markdown("# 👩 Yo Momma Jokes")

if st.button("Get Joke"):
    try:
        response = requests.get("https://yomomma-api.herokuapp.com/jokes")
        if response.status_code == 200:
            st.header(response.json()['joke'])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
