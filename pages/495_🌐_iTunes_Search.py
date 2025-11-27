import streamlit as st
import requests

st.set_page_config(page_title="iTunes Search", page_icon="🎵")
st.markdown("# 🎵 iTunes Search")

term = st.text_input("Artist/Song", "Taylor Swift")

if st.button("Search"):
    try:
        response = requests.get(f"https://itunes.apple.com/search?term={term}&limit=5")
        if response.status_code == 200:
            data = response.json()
            for item in data['results']:
                st.subheader(item.get('trackName', item.get('collectionName')))
                st.write(f"**Artist:** {item['artistName']}")
                if 'artworkUrl100' in item:
                    st.image(item['artworkUrl100'])
                if 'previewUrl' in item:
                    st.audio(item['previewUrl'])
    except Exception as e:
        st.error(f"Error: {e}")
