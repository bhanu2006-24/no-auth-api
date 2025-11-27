import streamlit as st
import requests

st.set_page_config(page_title="JokeAPI", page_icon="🤣")
st.markdown("# 🤣 JokeAPI")

if st.button("Get Joke"):
    try:
        response = requests.get("https://v2.jokeapi.dev/joke/Any?safe-mode")
        if response.status_code == 200:
            data = response.json()
            if data['type'] == 'single':
                st.write(data['joke'])
            else:
                st.write(data['setup'])
                st.write(f"**{data['delivery']}**")
    except Exception as e:
        st.error(f"Error: {e}")
