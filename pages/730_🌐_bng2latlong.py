import streamlit as st
import requests

st.set_page_config(page_title="BNG to LatLong", page_icon="🗺️")
st.markdown("# 🗺️ British National Grid to Lat/Long")

easting = st.number_input("Easting", value=530000)
northing = st.number_input("Northing", value=180000)

if st.button("Convert"):
    try:
        response = requests.get(f"https://api.getthedata.com/bng2latlong/{easting}/{northing}")
        if response.status_code == 200:
            data = response.json()
            st.json(data)
            if data['status'] == 'ok':
                st.metric("Latitude", data['latitude'])
                st.metric("Longitude", data['longitude'])
    except Exception as e:
        st.error(f"Error: {e}")
