import streamlit as st
import requests

st.set_page_config(page_title="Zip Code Info", page_icon="📮")

st.markdown("# 📮 Zip Code Info")
st.sidebar.header("Zip Code Info")
st.write(
    """This page fetches location information for a zip code using the [Zippopotam.us API](https://www.zippopotam.us/)."""
)

country = st.selectbox("Country", ["us", "gb", "de", "fr", "es", "it"])
zip_code = st.text_input("Enter Zip Code", "90210")

if st.button("Get Info"):
    if zip_code:
        try:
            response = requests.get(f"https://api.zippopotam.us/{country}/{zip_code}")
            if response.status_code == 200:
                data = response.json()
                place = data["places"][0]
                st.subheader(f"Location Info for {zip_code}, {country.upper()}")
                st.write(f"**Place Name:** {place['place name']}")
                st.write(f"**State:** {place['state']}")
                st.write(f"**Latitude:** {place['latitude']}")
                st.write(f"**Longitude:** {place['longitude']}")
            else:
                st.error("Zip code not found.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a zip code.")
