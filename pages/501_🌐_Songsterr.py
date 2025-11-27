import streamlit as st
import requests

st.set_page_config(page_title="Songsterr", page_icon="🎸")
st.markdown("# 🎸 Songsterr")

query = st.text_input("Song Title", "Stairway to Heaven")

if st.button("Search Tabs"):
    try:
        response = requests.get(f"https://www.songsterr.com/a/ra/songs.json?pattern={query}")
        if response.status_code == 200:
            data = response.json()
            for song in data[:5]:
                st.subheader(song['title'])
                st.write(f"**Artist:** {song['artist']['name']}")
                st.markdown(f"[View Tab](http://www.songsterr.com/a/wa/song?id={song['id']})")
    except Exception as e:
        st.error(f"Error: {e}")
