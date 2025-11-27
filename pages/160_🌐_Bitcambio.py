import streamlit as st
import requests

st.set_page_config(page_title="Bitcambio", page_icon="🇧🇷")

st.markdown("# 🇧🇷 Bitcambio Ticker")
st.write("Brazilian crypto exchange.")

if st.button("Get Ticker"):
    try:
        response = requests.get("https://nova.bitcambio.com.br/api/v3/public/getassets")
        if response.status_code == 200:
            data = response.json()
            st.dataframe(data['result'])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
