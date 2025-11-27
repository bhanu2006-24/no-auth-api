import streamlit as st
import requests

st.set_page_config(page_title="SHOUTCLOUD", page_icon="📢")

st.markdown("# 📢 SHOUTCLOUD")
st.write("ALL CAPS AS A SERVICE.")

text = st.text_input("Text", "hello world")

if st.button("SHOUT"):
    try:
        response = requests.post("HTTP://API.SHOUTCLOUD.IO/V1/SHOUT", json={"INPUT": text})
        if response.status_code == 200:
            st.header(response.json()['OUTPUT'])
        else:
            st.error("API ERROR")
    except Exception as e:
        st.error(f"ERROR: {e}")
