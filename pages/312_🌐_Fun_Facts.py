import streamlit as st
import requests

st.set_page_config(page_title="Fun Facts", page_icon="💡")
st.markdown("# 💡 Fun Facts")

if st.button("Get Fact"):
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        if response.status_code == 200:
            st.write(response.json()['text'])
    except Exception as e:
        st.error(f"Error: {e}")
