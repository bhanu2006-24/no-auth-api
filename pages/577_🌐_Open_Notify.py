import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="ISS Location", page_icon="🛰️")
st.markdown("# 🛰️ ISS Location")

if st.button("Track ISS"):
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        if response.status_code == 200:
            data = response.json()
            lat = float(data['iss_position']['latitude'])
            lon = float(data['iss_position']['longitude'])
            st.metric("Latitude", lat)
            st.metric("Longitude", lon)
            st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}))
    except Exception as e:
        st.error(f"Error: {e}")
