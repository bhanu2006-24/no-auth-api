import streamlit as st
import requests

st.set_page_config(page_title="Zen Quotes", page_icon="🧘")
st.markdown("# 🧘 Zen Quotes")

if st.button("Get Quote"):
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()
            data = data[0]
            st.write(f"**{data["q"]}**")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
