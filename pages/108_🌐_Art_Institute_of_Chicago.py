import streamlit as st
import requests

st.set_page_config(page_title="Art Institute of Chicago", page_icon="🎨")

st.markdown("# 🎨 Art Institute of Chicago")
st.write("Explore the collection.")

if st.button("Get Random Artwork"):
    try:
        # Get a random page to simulate random artwork
        import random
        page = random.randint(1, 100)
        response = requests.get(f"https://api.artic.edu/api/v1/artworks?page={page}&limit=1")
        if response.status_code == 200:
            data = response.json()
            artwork = data["data"][0]
            st.header(artwork["title"])
            st.write(f"**Artist:** {artwork['artist_display']}")
            st.write(f"**Date:** {artwork['date_display']}")
            st.write(f"**Medium:** {artwork['medium_display']}")
            
            if artwork["image_id"]:
                img_url = f"https://www.artic.edu/iiif/2/{artwork['image_id']}/full/843,/0/default.jpg"
                st.image(img_url, caption=artwork["title"], use_column_width=True)
            else:
                st.warning("No image available for this artwork.")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
