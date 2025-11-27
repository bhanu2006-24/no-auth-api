import streamlit as st
import requests
import random

st.set_page_config(page_title="The Met", page_icon="🏛️")

st.markdown("# 🏛️ The Metropolitan Museum of Art")
st.write("Explore the Met's collection.")

if st.button("Get Random Object"):
    try:
        # First get a list of object IDs (or just pick a random number range known to be valid, but searching is safer)
        # Let's search for "sunflowers" to get some IDs
        search_response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search?q=sunflowers&hasImages=true")
        if search_response.status_code == 200:
            ids = search_response.json()["objectIDs"]
            if ids:
                obj_id = random.choice(ids[:50]) # Pick from top 50
                
                obj_response = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}")
                if obj_response.status_code == 200:
                    obj = obj_response.json()
                    st.header(obj["title"])
                    st.write(f"**Artist:** {obj['artistDisplayName']}")
                    st.write(f"**Date:** {obj['objectDate']}")
                    st.write(f"**Medium:** {obj['medium']}")
                    st.image(obj["primaryImage"], use_column_width=True)
                else:
                    st.error("Failed to fetch object details.")
            else:
                st.warning("No objects found.")
        else:
            st.error("Search failed.")
    except Exception as e:
        st.error(f"Error: {e}")
