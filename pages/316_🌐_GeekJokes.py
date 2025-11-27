import streamlit as st
import requests

st.set_page_config(page_title="Geek Jokes", page_icon="🤓")
st.markdown("# 🤓 Geek Jokes")

if st.button("Get Joke"):
    try:
        response = requests.get("https://geek-jokes.sameerkumar.website/api?format=json")
        if response.status_code == 200:
            st.write(response.json()['joke'])
    except Exception as e:
        st.error(f"Error: {e}")
