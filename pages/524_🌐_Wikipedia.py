import streamlit as st
import requests

st.set_page_config(page_title="Wikipedia", page_icon="📚")
st.markdown("# 📚 Wikipedia")

query = st.text_input("Search", "Python (programming language)")

if st.button("Get Summary"):
    try:
        response = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}")
        if response.status_code == 200:
            data = response.json()
            st.header(data['title'])
            if 'thumbnail' in data:
                st.image(data['thumbnail']['source'])
            st.write(data['extract'])
        else:
            st.error("Page not found.")
    except Exception as e:
        st.error(f"Error: {e}")
