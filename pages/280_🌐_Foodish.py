import streamlit as st
import requests

st.set_page_config(page_title="Foodish", page_icon="🍲")

st.markdown("# 🍲 Foodish")
st.write("Random food images.")

if st.button("Get Food"):
    try:
        response = requests.get("https://foodish-api.com/api/")
        if response.status_code == 200:
            data = response.json()
            st.image(data['image'])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
