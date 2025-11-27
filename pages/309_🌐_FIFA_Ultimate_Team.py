import streamlit as st
import requests

st.set_page_config(page_title="FIFA UT", page_icon="⚽")
st.markdown("# ⚽ FIFA Ultimate Team")

if st.button("Get Items"):
    try:
        response = requests.get("https://futdb.app/api/items", headers={"X-AUTH-TOKEN": "YOUR_KEY_HERE"})
        st.warning("This API requires an API Key.")
    except Exception as e:
        st.error(f"Error: {e}")
