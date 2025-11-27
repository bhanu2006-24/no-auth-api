import streamlit as st
import requests

st.set_page_config(page_title="Postman Echo", page_icon="👨‍🚀")

st.markdown("# 👨‍🚀 Postman Echo")
st.write("Test your API calls.")

params = st.text_input("Query Params (e.g., foo=bar)", "foo=bar")

if st.button("Send GET Request"):
    try:
        response = requests.get(f"https://postman-echo.com/get?{params}")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
