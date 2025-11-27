import streamlit as st
import requests

st.set_page_config(page_title="Rick and Morty", page_icon="🧪")
st.markdown("# 🧪 Rick and Morty")

if st.button("Get Character"):
    try:
        import random
        id = random.randint(1, 800)
        response = requests.get(f"https://rickandmortyapi.com/api/character/{id}")
        if response.status_code == 200:
            data = response.json()
            st.header(data['name'])
            st.image(data['image'])
            st.write(f"**Status:** {data['status']}")
            st.write(f"**Species:** {data['species']}")
            st.write(f"**Origin:** {data['origin']['name']}")
    except Exception as e:
        st.error(f"Error: {e}")
