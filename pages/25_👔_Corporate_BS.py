import streamlit as st
import requests

st.set_page_config(page_title="Corporate BS", page_icon="👔")

st.markdown("# 👔 Corporate BS Generator")
st.sidebar.header("Corporate BS")
st.write(
    """This page generates random corporate buzzwords using the [Corporate BS Generator API](https://corporatebs-generator.sameerkumar.website/)."""
)

if st.button("Generate BS"):
    try:
        response = requests.get("https://corporatebs-generator.sameerkumar.website/")
        if response.status_code == 200:
            data = response.json()
            st.info(data["phrase"])
        else:
            st.error("Failed to fetch BS. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
