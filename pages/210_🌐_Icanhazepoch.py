import streamlit as st
import requests

st.set_page_config(page_title="Icanhazepoch", page_icon="🕒")

st.markdown("# 🕒 Icanhazepoch")
st.write("Get current epoch time.")

if st.button("Get Epoch"):
    try:
        response = requests.get("https://icanhazepoch.com")
        if response.status_code == 200:
            st.metric("Current Epoch", response.text)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
