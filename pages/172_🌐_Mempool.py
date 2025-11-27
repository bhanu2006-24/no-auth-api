import streamlit as st
import requests

st.set_page_config(page_title="Mempool.space", page_icon="🧠")

st.markdown("# 🧠 Mempool.space")
st.write("Bitcoin fees and block info.")

if st.button("Get Recommended Fees"):
    try:
        response = requests.get("https://mempool.space/api/v1/fees/recommended")
        if response.status_code == 200:
            data = response.json()
            col1, col2, col3 = st.columns(3)
            col1.metric("Fastest", f"{data['fastestFee']} sat/vB")
            col2.metric("Half Hour", f"{data['halfHourFee']} sat/vB")
            col3.metric("Hour", f"{data['hourFee']} sat/vB")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
