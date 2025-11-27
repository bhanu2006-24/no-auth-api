import streamlit as st
import requests

st.set_page_config(page_title="Random Duck", page_icon="🦆")

st.markdown("# 🦆 Random Duck")

if st.button("Quack!"):
    try:
        response = requests.get("https://random-d.uk/api/v2/random")
        if response.status_code == 200:
            data = response.json()
            st.image(data["url"], caption=data.get("message", "Quack!"), use_column_width=True)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
