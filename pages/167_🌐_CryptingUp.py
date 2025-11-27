import streamlit as st
import requests

st.set_page_config(page_title="CryptingUp", page_icon="🆙")

st.markdown("# 🆙 CryptingUp")

if st.button("Get Markets"):
    try:
        response = requests.get("https://www.cryptingup.com/api/markets")
        if response.status_code == 200:
            data = response.json()
            markets = data['markets'][:10]
            for m in markets:
                st.write(f"**{m['symbol']}:** ${m['price']}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
