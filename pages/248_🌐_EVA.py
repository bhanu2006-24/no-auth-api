import streamlit as st
import requests

st.set_page_config(page_title="EVA", page_icon="📧")

st.markdown("# 📧 EVA Email Verifier")

email = st.text_input("Email", "test@example.com")

if st.button("Verify"):
    try:
        response = requests.get(f"https://api.eva.pingutil.com/email?email={email}")
        if response.status_code == 200:
            data = response.json()
            st.json(data)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
