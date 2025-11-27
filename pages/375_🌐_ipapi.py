import streamlit as st
import requests

st.set_page_config(page_title="ipapi", page_icon="📍")
st.markdown("# 📍 ipapi")

if st.button("Check IP"):
    try:
        response = requests.get("https://ipapi.co/json/")
        if response.status_code == 200:
            st.json(response.json())
    except Exception as e:
        st.error(f"Error: {e}")
