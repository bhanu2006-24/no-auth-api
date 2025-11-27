import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="USGS Earthquakes", page_icon="🌍")

st.title("🌍 USGS Earthquake Data")
st.markdown("Get recent earthquake data using [USGS API](https://earthquake.usgs.gov/).")

min_magnitude = st.slider("Minimum Magnitude", 0.0, 10.0, 4.5)

if st.button("Get Earthquakes"):
    try:
        url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude={min_magnitude}&limit=20"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            features = data['features']
            
            if features:
                st.success(f"Found {len(features)} earthquakes.")
                
                eq_data = []
                for feature in features:
                    props = feature['properties']
                    coords = feature['geometry']['coordinates']
                    eq_data.append({
                        "Place": props['place'],
                        "Magnitude": props['mag'],
                        "Time": pd.to_datetime(props['time'], unit='ms'),
                        "URL": props['url'],
                        "lat": coords[1],
                        "lon": coords[0]
                    })
                
                df = pd.DataFrame(eq_data)
                
                # Display map
                st.map(df)
                
                # Display table
                st.dataframe(df[['Place', 'Magnitude', 'Time', 'URL']])
            else:
                st.warning("No earthquakes found with this magnitude.")
        else:
            st.error("Failed to fetch earthquake data.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
