import streamlit as st
import requests

st.set_page_config(page_title="Sunrise & Sunset", page_icon="🌅")

st.markdown("# 🌅 Sunrise & Sunset")
st.sidebar.header("Sunrise & Sunset")
st.write(
    """This page fetches solar data for a specific location using the [Sunrise-Sunset API](https://sunrise-sunset.org/api)."""
)

lat = st.number_input("Latitude", value=36.7201600)
lng = st.number_input("Longitude", value=-4.4203400)

if st.button("Get Solar Data"):
    try:
        response = requests.get(f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}")
        if response.status_code == 200:
            data = response.json()["results"]
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Sunrise", data["sunrise"])
                st.metric("Sunset", data["sunset"])
            with col2:
                st.metric("Day Length", data["day_length"])
                st.metric("Solar Noon", data["solar_noon"])
        else:
            st.error("Failed to fetch data. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
