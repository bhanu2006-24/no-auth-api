import streamlit as st
import requests

st.set_page_config(page_title="Tronald Dump", page_icon="🇺🇸")
st.markdown("# 🇺🇸 Tronald Dump")

if st.button("Get Quote"):
    try:
        response = requests.get("https://api.tronalddump.io/random/quote")
        if response.status_code == 200:
            st.write(response.json()['value'])
    except Exception as e:
        st.error(f"Error: {e}")
