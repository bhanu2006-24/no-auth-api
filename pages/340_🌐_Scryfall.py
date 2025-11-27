import streamlit as st
import requests

st.set_page_config(page_title="Scryfall", page_icon="🃏")
st.markdown("# 🃏 Scryfall (MTG)")

if st.button("Random Card"):
    try:
        response = requests.get("https://api.scryfall.com/cards/random")
        if response.status_code == 200:
            data = response.json()
            st.header(data['name'])
            if 'image_uris' in data:
                st.image(data['image_uris']['normal'])
            st.write(data.get('oracle_text', ''))
    except Exception as e:
        st.error(f"Error: {e}")
