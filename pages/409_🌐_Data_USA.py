import streamlit as st
import requests

st.set_page_config(page_title="Data USA", page_icon="🇺🇸")
st.markdown("# 🇺🇸 Data USA")

if st.button("Get Population Data"):
    try:
        response = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
        if response.status_code == 200:
            data = response.json()['data']
            st.dataframe(data)
    except Exception as e:
        st.error(f"Error: {e}")
