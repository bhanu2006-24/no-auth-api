import streamlit as st
import requests

st.set_page_config(page_title="Techy", page_icon="💻")

st.markdown("# 💻 Techy")
st.write("Tech jargon.")

if st.button("Get Message"):
    try:
        response = requests.get("https://techy-api.vercel.app/api/json")
        if response.status_code == 200:
            st.header(response.json()['message'])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
