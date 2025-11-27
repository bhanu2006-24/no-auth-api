import streamlit as st
import requests

st.set_page_config(page_title="Digimon TCG", page_icon="🃏")
st.markdown("# 🃏 Digimon TCG")

if st.button("Get All Cards (Limit 5)"):
    try:
        response = requests.get("https://digimoncard.io/api-public/getAllCards.php?sort=name&series=Digimon%20Card%20Game&sortdirection=asc")
        if response.status_code == 200:
            data = response.json()
            for card in data[:5]:
                st.subheader(card['name'])
                st.image(card['image_url'])
                st.write(f"**Type:** {card['type']}")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
