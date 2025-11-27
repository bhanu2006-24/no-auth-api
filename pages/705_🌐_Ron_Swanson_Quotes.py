import streamlit as st
import requests

st.set_page_config(page_title="Ron Swanson", page_icon="🥓")
st.markdown("# 🥓 Ron Swanson")

if st.button("Get Quote"):
    try:
        response = requests.get("https://ron-swanson-quotes.herokuapp.com/v2/quotes")
        if response.status_code == 200:
            data = response.json()
            data = data[0]
            st.write(data)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
