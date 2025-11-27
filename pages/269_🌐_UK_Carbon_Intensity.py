import streamlit as st
import requests

st.set_page_config(page_title="Carbon Intensity", page_icon="🇬🇧")

st.markdown("# 🇬🇧 UK Carbon Intensity")

if st.button("Get Current Intensity"):
    try:
        response = requests.get("https://api.carbonintensity.org.uk/intensity")
        if response.status_code == 200:
            data = response.json()['data'][0]
            st.metric("Index", data['intensity']['index'].upper())
            st.metric("Forecast", f"{data['intensity']['forecast']} gCO2/kWh")
            st.metric("Actual", f"{data['intensity']['actual']} gCO2/kWh")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
