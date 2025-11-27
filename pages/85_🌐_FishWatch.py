import streamlit as st
import requests

st.set_page_config(page_title="FishWatch", page_icon="🐟")

st.markdown("# 🐟 FishWatch Species")
st.sidebar.header("FishWatch")
st.write("Search for fish species data from NOAA.")

species = st.text_input("Enter Species Name (e.g., Red Snapper)", "Red Snapper")

if st.button("🔍 Search"):
    try:
        url = f"https://www.fishwatch.gov/api/species/{species}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                # API returns a list of dicts
                for fish in data:
                    st.subheader(fish.get("Species Name", "Unknown"))
                    
                    # Image
                    img_gallery = fish.get("Image Gallery")
                    if img_gallery:
                        if isinstance(img_gallery, list) and len(img_gallery) > 0:
                             st.image(img_gallery[0].get("src"), caption=img_gallery[0].get("alt"))
                        elif isinstance(img_gallery, dict):
                             st.image(img_gallery.get("src"), caption=img_gallery.get("alt"))

                    st.write(f"**Scientific Name:** {fish.get('Scientific Name')}")
                    st.write(f"**Habitat:** {fish.get('Habitat')}")
                    st.write(f"**Location:** {fish.get('Location')}")
                    
                    with st.expander("More Details"):
                        st.markdown(fish.get("Physical Description", ""))
                        st.markdown(f"**Population:** {fish.get('Population')}")
            else:
                st.warning("No fish found with that name.")
        else:
            st.error("API Error.")
    except Exception as e:
        st.error(f"Error: {e}")
