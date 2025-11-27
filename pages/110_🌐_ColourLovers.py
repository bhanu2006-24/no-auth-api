import streamlit as st
import requests

st.set_page_config(page_title="ColourLovers", page_icon="🎨")

st.markdown("# 🎨 ColourLovers Top Palettes")
st.write("Browse top palettes from ColourLovers.")

if st.button("Fetch Palettes"):
    try:
        # Note: ColourLovers API is HTTP
        response = requests.get("http://www.colourlovers.com/api/palettes/top?format=json", headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            palettes = response.json()
            for pal in palettes[:10]:
                st.subheader(pal["title"])
                st.write(f"By {pal['userName']}")
                st.image(pal["imageUrl"], use_column_width=True)
                st.markdown("---")
        else:
            st.error(f"API Error: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {e}")
