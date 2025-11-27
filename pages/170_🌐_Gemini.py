import streamlit as st
import requests

st.set_page_config(page_title="Gemini Exchange", page_icon="♊")

st.markdown("# ♊ Gemini Exchange")

if st.button("Get Ticker (BTCUSD)"):
    try:
        response = requests.get("https://api.gemini.com/v1/pubticker/btcusd")
        if response.status_code == 200:
            data = response.json()
            st.metric("BTC/USD", f"${data['last']}")
            st.write(f"**Bid:** {data['bid']}")
            st.write(f"**Ask:** {data['ask']}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
