import streamlit as st
import requests

st.set_page_config(page_title="Zippopotamus", page_icon="📮")
st.markdown("# 📮 Zippopotamus")

zipcode = st.text_input("US Zip Code", "90210")

if st.button("Lookup"):
    try:
        response = requests.get(f"https://api.zippopotam.us/us/{zipcode}")
        if response.status_code == 200:
            data = response.json()
            place = data['places'][0]
            st.write(f"**City:** {place['place name']}")
            st.write(f"**State:** {place['state']}")
    except Exception as e:
        st.error(f"Error: {e}")
