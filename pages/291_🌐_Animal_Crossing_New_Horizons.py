import streamlit as st
import requests

st.set_page_config(page_title="ACNH", page_icon="🏝️")

st.markdown("# 🏝️ Animal Crossing New Horizons")

if st.button("Get Fish"):
    try:
        response = requests.get("http://acnhapi.com/v1/fish/1")
        if response.status_code == 200:
            data = response.json()
            st.header(data['name']['name-USen'].capitalize())
            st.image(data['image_uri'])
            st.write(f"**Price:** {data['price']}")
            st.write(f"**Catch Phrase:** {data['catch-phrase']}")
        else:
            st.error("API Error (Service might be down)")
    except Exception as e:
        st.error(f"Error: {e}")
