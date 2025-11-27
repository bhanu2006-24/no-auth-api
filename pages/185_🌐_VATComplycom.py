import streamlit as st
import requests

st.set_page_config(page_title="VATComply", page_icon="💶")

st.markdown("# 💶 VATComply")
st.write("VAT rates and exchange rates.")

if st.button("Get Rates"):
    try:
        response = requests.get("https://api.vatcomply.com/rates")
        if response.status_code == 200:
            data = response.json()
            st.write(f"**Base:** {data['base']}")
            st.write(f"**Date:** {data['date']}")
            st.json(data['rates'])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
