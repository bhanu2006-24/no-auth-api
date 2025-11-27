import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="USGS Earthquakes", page_icon="🌋")
st.markdown("# 🌋 USGS Earthquakes")

if st.button("Get Recent Quakes"):
    try:
        response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")
        if response.status_code == 200:
            data = response.json()
            quakes = []
            for feature in data['features']:
                props = feature['properties']
                geom = feature['geometry']['coordinates']
                quakes.append({
                    'place': props['place'],
                    'mag': props['mag'],
                    'lat': geom[1],
                    'lon': geom[0]
                })
            df = pd.DataFrame(quakes)
            st.dataframe(df)
            st.map(df)
    except Exception as e:
        st.error(f"Error: {e}")
