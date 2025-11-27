import streamlit as st
import requests

st.set_page_config(page_title="IPify", page_icon="🔢")

st.markdown("# 🔢 IPify")
st.write("A simple IP address API.")

if st.button("Get IP"):
    try:
        response = requests.get("https://api.ipify.org?format=json")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
