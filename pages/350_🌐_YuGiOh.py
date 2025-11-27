import streamlit as st
import requests

st.set_page_config(page_title="Yu-Gi-Oh!", page_icon="🃏")
st.markdown("# 🃏 Yu-Gi-Oh!")

if st.button("Get Card"):
    try:
        response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php?num=1&offset=0") # Should randomize
        if response.status_code == 200:
            data = response.json()
            card = data['data'][0]
            st.header(card['name'])
            st.image(card['card_images'][0]['image_url'])
            st.write(f"**Type:** {card['type']}")
            st.write(card['desc'])
    except Exception as e:
        st.error(f"Error: {e}")
