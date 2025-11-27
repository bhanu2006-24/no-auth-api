import streamlit as st
import requests

st.set_page_config(page_title="CountAPI", page_icon="🔢")

st.markdown("# 🔢 CountAPI")
st.write("Simple hit counter.")

namespace = st.text_input("Namespace (e.g., mysite.com)", "test_namespace")
key = st.text_input("Key (e.g., visits)", "test_key")

if st.button("Hit Counter"):
    try:
        response = requests.get(f"https://api.countapi.xyz/hit/{namespace}/{key}")
        if response.status_code == 200:
            data = response.json()
            st.metric("Current Count", data['value'])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
