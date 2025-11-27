import streamlit as st
import requests

st.set_page_config(page_title="MCU", page_icon="🎬")
st.markdown("# 🎬 Next MCU Film")

if st.button("Check"):
    try:
        response = requests.get("https://whenisthenextmcufilm.com/api")
        if response.status_code == 200:
            data = response.json()
            st.header(data['title'])
            st.write(f"**Release Date:** {data['release_date']}")
            st.write(f"**Days Until:** {data['days_until']}")
            st.image(data['poster_url'])
            st.write(data['overview'])
    except Exception as e:
        st.error(f"Error: {e}")
