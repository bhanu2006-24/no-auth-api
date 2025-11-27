import streamlit as st
import requests

st.set_page_config(page_title="MMO Games", page_icon="🎮")
st.markdown("# 🎮 MMO Games")

if st.button("Get Live Games"):
    try:
        response = requests.get("https://www.mmobomb.com/api1/games")
        if response.status_code == 200:
            data = response.json()
            for game in data[:5]:
                st.subheader(game['title'])
                st.image(game['thumbnail'])
                st.write(game['short_description'])
    except Exception as e:
        st.error(f"Error: {e}")
