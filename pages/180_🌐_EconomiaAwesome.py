import streamlit as st
import requests

st.set_page_config(page_title="Economia Awesome", page_icon="💰")

st.markdown("# 💰 Economia Awesome")
st.write("Brazilian exchange rates.")

if st.button("Get Rates"):
    try:
        response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
        if response.status_code == 200:
            data = response.json()
            for key, val in data.items():
                st.metric(val['name'], f"R$ {val['bid']}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
