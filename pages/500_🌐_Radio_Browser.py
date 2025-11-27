import streamlit as st
import requests

st.set_page_config(page_title="Radio Browser", page_icon="📻")
st.markdown("# 📻 Radio Browser")

tag = st.text_input("Tag (e.g., jazz)", "jazz")

if st.button("Search Stations"):
    try:
        response = requests.get(f"https://de1.api.radio-browser.info/json/stations/bytag/{tag}?limit=5")
        if response.status_code == 200:
            data = response.json()
            for station in data:
                st.subheader(station['name'])
                if station['favicon']:
                    st.image(station['favicon'], width=50)
                st.audio(station['url'])
    except Exception as e:
        st.error(f"Error: {e}")
