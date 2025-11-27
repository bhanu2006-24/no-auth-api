import streamlit as st
import requests

st.set_page_config(page_title="xkcd", page_icon="🖼️")
st.markdown("# 🖼️ xkcd")

if st.button("Get Latest Comic"):
    try:
        response = requests.get("https://xkcd.com/info.0.json")
        if response.status_code == 200:
            data = response.json()
            st.header(data['title'])
            st.image(data['img'], caption=data['alt'])
    except Exception as e:
        st.error(f"Error: {e}")
