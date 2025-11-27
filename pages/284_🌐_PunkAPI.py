import streamlit as st
import requests

st.set_page_config(page_title="PunkAPI", page_icon="🍺")

st.markdown("# 🍺 PunkAPI (Brewdog)")

if st.button("Get Random Beer"):
    try:
        response = requests.get("https://api.punkapi.com/v2/beers/random")
        if response.status_code == 200:
            beer = response.json()[0]
            st.header(beer['name'])
            st.caption(beer['tagline'])
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(beer['image_url'], width=100)
            with col2:
                st.write(beer['description'])
                st.write(f"**ABV:** {beer['abv']}%")
        else:
            st.error("API Error (Service might be down)")
    except Exception as e:
        st.error(f"Error: {e}")
