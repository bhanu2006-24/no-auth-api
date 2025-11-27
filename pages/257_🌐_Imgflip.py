import streamlit as st
import requests

st.set_page_config(page_title="Imgflip", page_icon="🖼️")

st.markdown("# 🖼️ Imgflip Memes")

if st.button("Get Popular Memes"):
    try:
        response = requests.get("https://api.imgflip.com/get_memes")
        if response.status_code == 200:
            data = response.json()
            memes = data['data']['memes'][:10]
            for meme in memes:
                st.subheader(meme['name'])
                st.image(meme['url'], width=300)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
