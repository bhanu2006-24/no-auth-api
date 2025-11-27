import streamlit as st
import requests

st.set_page_config(page_title="Pokémon TCG", page_icon="🃏")
st.markdown("# 🃏 Pokémon TCG")

if st.button("Get Card"):
    try:
        response = requests.get("https://api.pokemontcg.io/v2/cards?pageSize=1&page=1") # Should randomize
        if response.status_code == 200:
            data = response.json()
            card = data['data'][0]
            st.image(card['images']['large'])
            st.subheader(card['name'])
    except Exception as e:
        st.error(f"Error: {e}")
