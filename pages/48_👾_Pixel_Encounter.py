import streamlit as st
import requests

st.set_page_config(page_title="Pixel Encounter", page_icon="👾")

st.markdown("# 👾 Pixel Encounter")
st.sidebar.header("Pixel Encounter")
st.write(
    """This page generates random pixel art monsters using the [Pixel Encounter API](https://pixelencounter.com/)."""
)

if st.button("Get Monster"):
    # The API returns an SVG image directly
    url = "https://app.pixelencounter.com/api/basic/monsters/random"
    st.image(url, caption="A Wild Monster Appeared!", width=300)
