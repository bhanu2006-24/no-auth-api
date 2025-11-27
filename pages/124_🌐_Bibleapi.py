import streamlit as st
import requests

st.set_page_config(page_title="Bible API", page_icon="📖")

st.markdown("# 📖 Bible Verses")
st.write("Search for Bible verses.")

query = st.text_input("Enter Reference (e.g., John 3:16)", "John 3:16")

if st.button("Get Verse"):
    try:
        response = requests.get(f"https://bible-api.com/{query}")
        if response.status_code == 200:
            data = response.json()
            st.markdown(f"### {data['reference']}")
            st.markdown(f"*{data['text']}*")
            st.caption(f"Translation: {data['translation_name']}")
        else:
            st.error("Verse not found.")
    except Exception as e:
        st.error(f"Error: {e}")
