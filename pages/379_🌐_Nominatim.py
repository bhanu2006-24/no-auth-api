import streamlit as st
import requests

st.set_page_config(page_title="Nominatim", page_icon="🗺️")
st.markdown("# 🗺️ Nominatim (OSM)")

query = st.text_input("Address", "1600 Pennsylvania Ave NW, Washington, DC")

if st.button("Geocode"):
    try:
        response = requests.get(f"https://nominatim.openstreetmap.org/search?q={query}&format=json", headers={'User-Agent': 'StreamlitApp'})
        if response.status_code == 200:
            data = response.json()
            if data:
                st.write(f"**Lat:** {data[0]['lat']}, **Lon:** {data[0]['lon']}")
                st.write(data[0]['display_name'])
            else:
                st.warning("Not found.")
    except Exception as e:
        st.error(f"Error: {e}")
