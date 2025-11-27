import streamlit as st
import requests

st.set_page_config(page_title="PurgoMalum", page_icon="🤬")

st.markdown("# 🤬 PurgoMalum")
st.write("Profanity filter.")

text = st.text_area("Enter Text", "This is some test text.")

if st.button("Filter"):
    try:
        response = requests.get(f"https://www.purgomalum.com/service/json?text={text}")
        if response.status_code == 200:
            data = response.json()
            st.success(data['result'])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
