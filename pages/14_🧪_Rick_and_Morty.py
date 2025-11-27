import streamlit as st
import requests

st.set_page_config(page_title="Rick and Morty", page_icon="🧪")

st.markdown("# 🧪 Rick and Morty Characters")
st.sidebar.header("Rick and Morty")
st.write(
    """This page fetches character information from the [Rick and Morty API](https://rickandmortyapi.com/)."""
)

char_id = st.number_input("Enter Character ID (1-826)", min_value=1, max_value=826, value=1)

if st.button("Get Character"):
    try:
        response = requests.get(f"https://rickandmortyapi.com/api/character/{char_id}")
        if response.status_code == 200:
            data = response.json()
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(data["image"], width=200)
            
            with col2:
                st.subheader(data["name"])
                st.write(f"**Status:** {data['status']}")
                st.write(f"**Species:** {data['species']}")
                st.write(f"**Gender:** {data['gender']}")
                st.write(f"**Origin:** {data['origin']['name']}")
        else:
            st.error("Failed to fetch character. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
