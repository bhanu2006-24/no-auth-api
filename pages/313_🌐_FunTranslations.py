import streamlit as st
import requests

st.set_page_config(page_title="FunTranslations", page_icon="🗣️")
st.markdown("# 🗣️ FunTranslations")

text = st.text_input("Text to Translate", "Hello World")
type = st.selectbox("Type", ["yoda", "pirate", "valyrian"])

if st.button("Translate"):
    try:
        response = requests.get(f"https://api.funtranslations.com/translate/{type}.json?text={text}")
        if response.status_code == 200:
            st.success(response.json()['contents']['translated'])
        elif response.status_code == 429:
            st.error("Rate limit exceeded.")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
