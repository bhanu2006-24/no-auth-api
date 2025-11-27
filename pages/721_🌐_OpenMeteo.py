import streamlit as st
import requests

st.set_page_config(page_title="Open-Meteo", page_icon="🌦️")
st.markdown("# 🌦️ Open-Meteo")

lat = st.number_input("Latitude", value=52.52)
lon = st.number_input("Longitude", value=13.41)

if st.button("Get Weather"):
    try:
        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")
        if response.status_code == 200:
            data = response.json()
            cw = data['current_weather']
            st.metric("Temperature", f"{cw['temperature']}°C")
            st.metric("Wind Speed", f"{cw['windspeed']} km/h")
    except Exception as e:
        st.error(f"Error: {e}")
