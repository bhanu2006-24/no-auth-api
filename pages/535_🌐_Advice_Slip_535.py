import streamlit as st
import requests

st.set_page_config(page_title="Advice Slip", page_icon="💡")
st.markdown("# 💡 Advice Slip")

if st.button("Get Quote"):
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        if response.status_code == 200:
            data = response.json()
            st.write(f"**{data["advice"]}**")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
