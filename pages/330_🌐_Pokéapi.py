import streamlit as st
import requests

st.set_page_config(page_title="PokéAPI", page_icon="🔴")
st.markdown("# 🔴 PokéAPI")

name = st.text_input("Pokemon Name", "pikachu")

if st.button("Search"):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
        if response.status_code == 200:
            data = response.json()
            st.header(data['name'].capitalize())
            st.image(data['sprites']['front_default'])
            st.write(f"**Height:** {data['height']}")
            st.write(f"**Weight:** {data['weight']}")
            types = [t['type']['name'] for t in data['types']]
            st.write(f"**Types:** {', '.join(types)}")
        else:
            st.error("Pokemon not found.")
    except Exception as e:
        st.error(f"Error: {e}")
