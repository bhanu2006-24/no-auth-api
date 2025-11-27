import streamlit as st
import requests

st.set_page_config(page_title="Httpbin", page_icon="🗑️")

st.markdown("# 🗑️ Httpbin")
st.write("A simple HTTP request & response service.")

if st.button("Send GET Request"):
    try:
        response = requests.get("https://httpbin.org/get", params={"test": "value"})
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
