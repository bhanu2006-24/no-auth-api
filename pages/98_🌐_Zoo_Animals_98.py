import streamlit as st
import requests

st.set_page_config(page_title="Zoo Animals", page_icon="🦁")

st.markdown("# 🦁 Zoo Animals")

if st.button("Get Random Animal"):
    try:
        response = requests.get("https://zoo-animal-api.herokuapp.com/animals/rand")
        if response.status_code == 200:
            data = response.json()
            st.header(data["name"])
            st.image(data["image_link"], caption=data["name"], use_column_width=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Latin Name:** {data['latin_name']}")
                st.write(f"**Animal Type:** {data['animal_type']}")
                st.write(f"**Active Time:** {data['active_time']}")
            with col2:
                st.write(f"**Lifespan:** {data['lifespan']} years")
                st.write(f"**Diet:** {data['diet']}")
                st.write(f"**Habitat:** {data['habitat']}")
                
            st.write(f"**Range:** {data['geo_range']}")
        else:
            st.error("API Error (The Zoo Animal API is often down/slow).")
    except Exception as e:
        st.error(f"Error: {e}")
