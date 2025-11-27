import streamlit as st
import requests

st.set_page_config(page_title="Random Jokes", page_icon="😂")

st.markdown("# 😂 Random Jokes")
st.sidebar.header("Random Jokes")
st.write(
    """This page fetches a random joke from the [Official Joke API](https://github.com/15Dkatz/official_joke_api)."""
)

if st.button("Tell me a joke"):
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            data = response.json()
            st.markdown(f"### {data['setup']}")
            st.markdown(f"**{data['punchline']}**")
        else:
            st.error("Failed to fetch joke. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
