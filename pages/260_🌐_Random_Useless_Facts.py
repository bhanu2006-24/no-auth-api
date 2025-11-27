import streamlit as st
import requests

st.set_page_config(page_title="Useless Facts", page_icon="🤔")

st.markdown("# 🤔 Useless Facts")

if st.button("Get Fact"):
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        if response.status_code == 200:
            data = response.json()
            st.write(data['text'])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
