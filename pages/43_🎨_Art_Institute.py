import streamlit as st
import requests

st.set_page_config(page_title="Art Institute", page_icon="🎨")

st.markdown("# 🎨 Art Institute of Chicago")
st.sidebar.header("Art Institute")
st.write(
    """This page fetches artworks from the [Art Institute of Chicago API](https://api.artic.edu/docs/)."""
)

if st.button("Get Artworks"):
    try:
        response = requests.get("https://api.artic.edu/api/v1/artworks?limit=5")
        if response.status_code == 200:
            data = response.json()
            config = data["config"]
            iiif_url = config["iiif_url"]
            
            for artwork in data["data"]:
                st.subheader(artwork["title"])
                st.write(f"**Artist:** {artwork['artist_display']}")
                st.write(f"**Date:** {artwork['date_display']}")
                
                image_id = artwork["image_id"]
                if image_id:
                    image_url = f"{iiif_url}/{image_id}/full/843,/0/default.jpg"
                    st.image(image_url, caption=artwork["title"], use_column_width=True)
                st.markdown("---")
        else:
            st.error("Failed to fetch artworks. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
