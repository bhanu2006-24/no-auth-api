import streamlit as st
import requests

st.set_page_config(page_title="FreeGeoIP", page_icon="📍")
st.markdown("# 📍 FreeGeoIP")

if st.button("Check IP"):
    try:
        response = requests.get("https://freegeoip.app/json/")
        if response.status_code == 200:
            st.json(response.json())
    except Exception as e:
        st.error(f"Error: {e}")
