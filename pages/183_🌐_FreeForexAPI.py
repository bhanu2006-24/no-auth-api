import streamlit as st
import requests

st.set_page_config(page_title="FreeForexAPI", page_icon="💱")

st.markdown("# 💱 FreeForexAPI")

if st.button("Get Quote (EUR/USD)"):
    try:
        response = requests.get("https://www.freeforexapi.com/api/live?pairs=EURUSD")
        if response.status_code == 200:
            data = response.json()
            if data['code'] == 200:
                st.metric("EUR/USD", data['rates']['EURUSD']['rate'])
            else:
                st.error("API Error")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
