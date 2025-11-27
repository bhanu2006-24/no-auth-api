import streamlit as st
import requests

st.set_page_config(page_title="Coinpaprika", page_icon="🌶️")

st.markdown("# 🌶️ Coinpaprika")

if st.button("Get Market Overview"):
    try:
        response = requests.get("https://api.coinpaprika.com/v1/global")
        if response.status_code == 200:
            data = response.json()
            st.metric("Market Cap (USD)", f"${data['market_cap_usd']:,}")
            st.metric("Volume 24h (USD)", f"${data['volume_24h_usd']:,}")
            st.metric("Bitcoin Dominance", f"{data['bitcoin_dominance_percentage']}%")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
