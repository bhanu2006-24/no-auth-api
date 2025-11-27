import streamlit as st
import requests

st.set_page_config(page_title="Motivational", page_icon="💪")
st.markdown("# 💪 Motivational")

if st.button("Get Quote"):
    try:
        response = requests.get("https://api.goprogram.ai/inspiration")
        if response.status_code == 200:
            data = response.json()
            st.write(f"**{data["quote"]}**")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
