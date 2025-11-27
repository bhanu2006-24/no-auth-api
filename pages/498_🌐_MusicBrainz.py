import streamlit as st
import requests

st.set_page_config(page_title="MusicBrainz", page_icon="🧠")
st.markdown("# 🧠 MusicBrainz")

artist = st.text_input("Artist Name", "Nirvana")

if st.button("Search"):
    try:
        response = requests.get(f"https://musicbrainz.org/ws/2/artist/?query={artist}&fmt=json")
        if response.status_code == 200:
            data = response.json()
            for artist in data['artists'][:5]:
                st.subheader(artist['name'])
                st.write(f"**Country:** {artist.get('country', 'Unknown')}")
                st.write(f"**Tags:** {', '.join([t['name'] for t in artist.get('tags', [])[:5]])}")
    except Exception as e:
        st.error(f"Error: {e}")
