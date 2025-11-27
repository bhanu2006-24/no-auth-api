import streamlit as st
import requests

st.set_page_config(page_title="Waifu.pics", page_icon="🖼️")

st.markdown("# 🖼️ Waifu.pics")
st.write("More Waifu pictures.")

category = st.selectbox("Category", ["waifu", "neko", "shinobu", "megumin", "bully", "cuddle", "cry", "hug", "awoo", "kiss", "lick", "pat", "smug", "bonk", "yeet", "blush", "smile", "wave", "highfive", "handhold", "nom", "bite", "glomp", "slap", "kill", "kick", "happy", "wink", "poke", "dance", "cringe"])

if st.button("Get Picture"):
    try:
        response = requests.get(f"https://api.waifu.pics/sfw/{category}")
        if response.status_code == 200:
            data = response.json()
            st.image(data["url"], caption=f"Category: {category}", use_column_width=True)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
