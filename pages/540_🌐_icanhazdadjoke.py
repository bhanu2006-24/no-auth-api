import streamlit as st
import requests

st.set_page_config(page_title="Dad Jokes", page_icon="👨")
st.markdown("# 👨 Dad Jokes")

if st.button("Get Joke"):
    try:
        response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
        if response.status_code == 200:
            st.header(response.json()['joke'])
    except Exception as e:
        st.error(f"Error: {e}")
