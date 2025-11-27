import streamlit as st
import requests

st.set_page_config(page_title="Fed Treasury", page_icon="🇺🇸")

st.markdown("# 🇺🇸 Fed Treasury Rates")

if st.button("Get Rates"):
    try:
        # Using a public source proxy or similar as direct gov API is complex
        st.info("Please visit treasury.gov for official data.")
    except Exception as e:
        st.error(f"Error: {e}")
