import streamlit as st
import requests

st.set_page_config(page_title="Icanhazip", page_icon="📍")

st.markdown("# 📍 Icanhazip")
st.write("Get your public IP address.")

if st.button("Get IP"):
    try:
        response = requests.get("https://icanhazip.com")
        if response.status_code == 200:
            st.metric("Your IP", response.text.strip())
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
