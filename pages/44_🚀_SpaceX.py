import streamlit as st
import requests

st.set_page_config(page_title="SpaceX", page_icon="🚀")

st.markdown("# 🚀 SpaceX Latest Launch")
st.sidebar.header("SpaceX")
st.write(
    """This page fetches the latest SpaceX launch information using the [SpaceX API](https://github.com/r-spacex/SpaceX-API)."""
)

if st.button("Get Latest Launch"):
    try:
        response = requests.get("https://api.spacexdata.com/v4/launches/latest")
        if response.status_code == 200:
            data = response.json()
            st.header(data["name"])
            st.write(f"**Date:** {data['date_utc']}")
            st.write(f"**Details:** {data['details']}")
            
            if data["links"]["patch"]["large"]:
                st.image(data["links"]["patch"]["large"], width=300)
            
            if data["links"]["webcast"]:
                st.video(data["links"]["webcast"])
        else:
            st.error("Failed to fetch launch data. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
