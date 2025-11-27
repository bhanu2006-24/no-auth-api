import streamlit as st
import requests

st.set_page_config(page_title="Dog Images", page_icon="🐩")

st.markdown("# 🐩 Random Dog Images")
st.sidebar.header("Dog Images")

if st.button("🐩 Show me a Dog"):
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        if response.status_code == 200:
            data = response.json()
            st.image(data["message"], caption="Good Boy!", use_column_width=True)
        else:
            st.error("API Error.")
    except Exception as e:
        st.error(f"Error: {e}")
