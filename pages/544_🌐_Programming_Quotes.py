import streamlit as st
import requests

st.set_page_config(page_title="Programming Quotes", page_icon="💻")
st.markdown("# 💻 Programming Quotes")

if st.button("Get Quote"):
    try:
        response = requests.get("https://programming-quotes-api.herokuapp.com/quotes/random")
        if response.status_code == 200:
            data = response.json()
            st.write(f"**{data["en"]}**")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
