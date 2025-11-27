import streamlit as st
import requests

st.set_page_config(page_title="Lyrics Search", page_icon="🎵")

st.title("🎵 Song Lyrics Search")
st.markdown("Search for song lyrics using [Lyrics.ovh](https://lyrics.ovh/).")

artist = st.text_input("Artist", "Coldplay")
title = st.text_input("Song Title", "Yellow")

if st.button("Get Lyrics"):
    if artist and title:
        try:
            response = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{title}")
            if response.status_code == 200:
                data = response.json()
                lyrics = data.get('lyrics', '')
                if lyrics:
                    st.subheader(f"{title} by {artist}")
                    st.text(lyrics)
                else:
                    st.warning("Lyrics not found.")
            else:
                st.error("Lyrics not found.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter both artist and song title.")
