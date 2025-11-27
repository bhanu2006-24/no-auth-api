import streamlit as st
import requests

st.set_page_config(page_title="Weather", page_icon="🌤️")

st.markdown("# 🌤️ Weather Forecast")
st.sidebar.header("Weather")
st.write(
    """This page fetches weather forecast using the [Open-Meteo API](https://open-meteo.com/)."""
)

lat = st.number_input("Latitude", value=52.52)
lon = st.number_input("Longitude", value=13.41)

if st.button("Get Weather"):
    try:
        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")
        if response.status_code == 200:
            data = response.json()
            current = data["current_weather"]
            st.metric("Temperature", f"{current['temperature']}°C")
            st.metric("Wind Speed", f"{current['windspeed']} km/h")
            st.write(f"**Time:** {current['time']}")
        else:
            st.error("Failed to fetch weather. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
