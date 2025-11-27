import streamlit as st
import requests

st.set_page_config(page_title="Coinlore", page_icon="📊")

st.markdown("# 📊 Coinlore Market Data")

if st.button("Get Top Coins"):
    try:
        response = requests.get("https://api.coinlore.net/api/tickers/")
        if response.status_code == 200:
            data = response.json()
            for coin in data['data'][:10]:
                st.metric(f"{coin['name']} ({coin['symbol']})", f"${coin['price_usd']}", f"{coin['percent_change_24h']}%")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
