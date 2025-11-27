import streamlit as st
import requests

st.set_page_config(page_title="Lyrics.ovh", page_icon="🎤")
st.markdown("# 🎤 Lyrics.ovh")

artist = st.text_input("Artist", "Coldplay")
title = st.text_input("Title", "Yellow")

if st.button("Get Lyrics"):
    try:
        response = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{title}")
        if response.status_code == 200:
            data = response.json()
            st.text(data['lyrics'])
        else:
            st.error("Lyrics not found.")
    except Exception as e:
        st.error(f"Error: {e}")
