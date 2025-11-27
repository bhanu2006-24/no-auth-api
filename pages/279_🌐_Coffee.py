import streamlit as st
import requests

st.set_page_config(page_title="Coffee", page_icon="☕")

st.markdown("# ☕ Random Coffee")

if st.button("Get Coffee"):
    try:
        response = requests.get("https://coffee.alexflipnote.dev/random.json")
        if response.status_code == 200:
            data = response.json()
            st.image(data['file'])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
