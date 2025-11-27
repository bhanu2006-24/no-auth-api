import streamlit as st
import requests

st.set_page_config(page_title="IP Info", page_icon="📍")

st.markdown("# 📍 IP Info")
st.sidebar.header("IP Info")
st.write(
    """This page fetches information about your IP address using the [ipapi API](https://ipapi.co/)."""
)

if st.button("Get IP Info"):
    try:
        response = requests.get("https://ipapi.co/json/")
        if response.status_code == 200:
            data = response.json()
            st.json(data)
            if "latitude" in data and "longitude" in data:
                st.map({"lat": [data["latitude"]], "lon": [data["longitude"]]})
        else:
            st.error("Failed to fetch IP info. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
