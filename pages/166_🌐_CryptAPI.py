import streamlit as st
import requests

st.set_page_config(page_title="CryptAPI", page_icon="💳")

st.markdown("# 💳 CryptAPI")
st.write("Crypto payment gateway info.")

if st.button("Get Supported Coins"):
    try:
        response = requests.get("https://cryptapi.io/api/info/")
        if response.status_code == 200:
            data = response.json()
            st.json(data)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
