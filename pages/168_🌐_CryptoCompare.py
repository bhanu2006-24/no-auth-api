import streamlit as st
import requests

st.set_page_config(page_title="CryptoCompare", page_icon="⚖️")

st.markdown("# ⚖️ CryptoCompare")

if st.button("Get Price (BTC/USD)"):
    try:
        response = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR")
        if response.status_code == 200:
            data = response.json()
            st.json(data)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
