import streamlit as st
import requests

st.set_page_config(page_title="Fun Facts", page_icon="💡")

st.markdown("# 💡 Random Fun Fact")

if st.button("Get Fact"):
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        if response.status_code == 200:
            data = response.json()
            st.header(data['text'])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
