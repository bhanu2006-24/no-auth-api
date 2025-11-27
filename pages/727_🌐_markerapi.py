import streamlit as st
import requests

st.set_page_config(page_title="MarkerAPI", page_icon="®️")
st.markdown("# ®️ MarkerAPI (Trademark Search)")

search = st.text_input("Search Trademark", "Apple")

if st.button("Search"):
    st.info("This API often requires specific headers or has changed. Displaying link.")
    st.markdown(f"[Search on MarkerAPI](https://markerapi.com/search/{search})")
