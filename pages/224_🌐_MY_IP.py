import streamlit as st
import requests

st.set_page_config(page_title="My IP", page_icon="📍")

st.markdown("# 📍 My IP")

if st.button("Check IP"):
    try:
        response = requests.get("https://api.myip.com")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
