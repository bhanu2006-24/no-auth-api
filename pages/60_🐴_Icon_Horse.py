import streamlit as st
import requests

st.set_page_config(page_title="Icon Horse", page_icon="🐴")

st.title("🐴 Icon Horse Favicon Fetcher")
st.markdown("Get the favicon of any website using [Icon Horse](https://icon.horse/).")

website_url = st.text_input("Enter Website URL (e.g., google.com)", "github.com")

if st.button("Get Favicon"):
    if website_url:
        # Icon Horse returns the image directly
        icon_url = f"https://icon.horse/icon/{website_url}"
        st.image(icon_url, caption=f"Favicon for {website_url}", width=100)
    else:
        st.warning("Please enter a URL.")
