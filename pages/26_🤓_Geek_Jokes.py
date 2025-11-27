import streamlit as st
import requests

st.set_page_config(page_title="Geek Jokes", page_icon="🤓")

st.markdown("# 🤓 Geek Jokes")
st.sidebar.header("Geek Jokes")
st.write(
    """This page fetches a random geek joke from the [Geek Joke API](https://github.com/sameerkumar18/geek-joke-api)."""
)

if st.button("Tell me a joke"):
    try:
        response = requests.get("https://geek-jokes.sameerkumar.website/api?format=json")
        if response.status_code == 200:
            data = response.json()
            st.success(data["joke"])
        else:
            st.error("Failed to fetch joke. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
