import streamlit as st
import requests

st.set_page_config(page_title="BitcoinCharts", page_icon="📈")

st.markdown("# 📈 BitcoinCharts")
st.write("Market data.")

if st.button("Get Weighted Prices"):
    try:
        response = requests.get("https://api.bitcoincharts.com/v1/weighted_prices.json")
        if response.status_code == 200:
            data = response.json()
            # Show a few major currencies
            majors = {k: v for k, v in data.items() if k in ['USD', 'EUR', 'GBP', 'JPY']}
            st.json(majors)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
