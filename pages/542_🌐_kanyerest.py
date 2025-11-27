import streamlit as st
import requests

st.set_page_config(page_title="Kanye Rest", page_icon="🎤")
st.markdown("# 🎤 Kanye Rest")

if st.button("Get Quote"):
    try:
        response = requests.get("https://api.kanye.rest/")
        if response.status_code == 200:
            data = response.json()
            st.write(f"**{data["quote"]}**")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
