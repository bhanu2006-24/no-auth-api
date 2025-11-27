import streamlit as st
import requests

st.set_page_config(page_title="Czech National Bank", page_icon="🇨🇿")

st.markdown("# 🇨🇿 Czech National Bank")
st.write("Exchange rates.")

if st.button("Get Rates"):
    try:
        response = requests.get("https://www.cnb.cz/en/financial-markets/foreign-exchange-market/central-bank-exchange-rate-fixing/central-bank-exchange-rate-fixing/daily.txt")
        if response.status_code == 200:
            st.text(response.text)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
