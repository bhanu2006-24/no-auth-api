import streamlit as st
import requests

st.set_page_config(page_title="Open Brewery DB", page_icon="🍺")

st.markdown("# 🍺 Open Brewery DB")

city = st.text_input("City", "San Diego")

if st.button("Search Breweries"):
    try:
        response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_city={city}&per_page=5")
        if response.status_code == 200:
            data = response.json()
            for brew in data:
                st.subheader(brew['name'])
                st.write(f"**Type:** {brew['brewery_type']}")
                st.write(f"**Address:** {brew.get('address_1', '')}")
                st.markdown(f"[Website]({brew.get('website_url', '#')})")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
