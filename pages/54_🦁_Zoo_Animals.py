import streamlit as st
import requests

st.set_page_config(page_title="Zoo Animals", page_icon="🦁")

st.title("🦁 Zoo Animals")
st.markdown("Fetch random facts and images of zoo animals using the [Zoo Animal API](https://zoo-animal-api.herokuapp.com/).")

if st.button("Get Random Animal"):
    try:
        response = requests.get("https://zoo-animal-api.herokuapp.com/animals/rand")
        if response.status_code == 200:
            data = response.json()
            st.subheader(data['name'])
            st.image(data['image_link'], caption=data['name'], use_column_width=True)
            
            st.markdown(f"**Latin Name:** {data['latin_name']}")
            st.markdown(f"**Animal Type:** {data['animal_type']}")
            st.markdown(f"**Active Time:** {data['active_time']}")
            st.markdown(f"**Min Length:** {data['length_min']} ft")
            st.markdown(f"**Max Length:** {data['length_max']} ft")
            st.markdown(f"**Min Weight:** {data['weight_min']} lbs")
            st.markdown(f"**Max Weight:** {data['weight_max']} lbs")
            st.markdown(f"**Lifespan:** {data['lifespan']} years")
            st.markdown(f"**Habitat:** {data['habitat']}")
            st.markdown(f"**Diet:** {data['diet']}")
            st.markdown(f"**Geo Range:** {data['geo_range']}")
        else:
            st.error("Failed to fetch animal data. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
