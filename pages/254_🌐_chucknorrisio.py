import streamlit as st
import requests

st.set_page_config(page_title="Chuck Norris", page_icon="🤠")

st.markdown("# 🤠 Chuck Norris Facts")

if st.button("Get Fact"):
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        if response.status_code == 200:
            data = response.json()
            st.image(data['icon_url'])
            st.header(data['value'])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
