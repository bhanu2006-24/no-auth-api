import streamlit as st
import requests

st.set_page_config(page_title="Mercado Bitcoin", page_icon="🇧🇷")

st.markdown("# 🇧🇷 Mercado Bitcoin")

if st.button("Get Ticker (BTC)"):
    try:
        response = requests.get("https://www.mercadobitcoin.net/api/BTC/ticker/")
        if response.status_code == 200:
            data = response.json()['ticker']
            st.metric("BTC/BRL", f"R$ {data['last']}")
            st.write(f"**High:** {data['high']}")
            st.write(f"**Low:** {data['low']}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
