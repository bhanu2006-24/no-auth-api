import streamlit as st
import requests

st.set_page_config(page_title="Random Fox", page_icon="🦊")

st.markdown("# 🦊 Random Fox")

if st.button("What does the fox say?"):
    try:
        response = requests.get("https://randomfox.ca/floof/")
        if response.status_code == 200:
            data = response.json()
            st.image(data["image"], use_column_width=True)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
