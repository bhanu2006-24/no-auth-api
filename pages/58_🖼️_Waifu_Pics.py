import streamlit as st
import requests

st.set_page_config(page_title="Waifu Pics", page_icon="🖼️")

st.title("🖼️ Waifu Pics")
st.markdown("Get random anime images using [Waifu.pics](https://waifu.pics/).")

category = st.selectbox("Select Category", ["waifu", "neko", "shinobu", "megumin", "bully", "cuddle", "cry", "hug", "awoo", "kiss", "lick", "pat", "smug", "bonk", "yeet", "blush", "smile", "wave", "highfive", "handhold", "nom", "bite", "glomp", "slap", "kill", "kick", "happy", "wink", "poke", "dance", "cringe"])

if st.button("Get Image"):
    try:
        response = requests.get(f"https://api.waifu.pics/sfw/{category}")
        if response.status_code == 200:
            data = response.json()
            st.image(data['url'], caption=f"Random {category}", use_column_width=True)
        else:
            st.error("Failed to fetch image.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
