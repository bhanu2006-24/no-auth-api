import streamlit as st
import requests

st.set_page_config(page_title="MTG", page_icon="🃏")
st.markdown("# 🃏 Magic: The Gathering")

if st.button("Get Card"):
    try:
        response = requests.get("https://api.magicthegathering.io/v1/cards?pageSize=1&random=true")
        if response.status_code == 200:
            data = response.json()
            if data['cards']:
                card = data['cards'][0]
                st.header(card['name'])
                if 'imageUrl' in card:
                    st.image(card['imageUrl'])
                st.write(card.get('text', ''))
    except Exception as e:
        st.error(f"Error: {e}")
