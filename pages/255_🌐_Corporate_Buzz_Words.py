import streamlit as st
import requests

st.set_page_config(page_title="Corporate Buzzwords", page_icon="👔")

st.markdown("# 👔 Corporate Buzzwords")

if st.button("Generate Phrase"):
    try:
        response = requests.get("https://corporatebs-generator.sameerkumar.website/")
        if response.status_code == 200:
            data = response.json()
            st.header(data['phrase'])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
