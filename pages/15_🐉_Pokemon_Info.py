import streamlit as st
import requests

st.set_page_config(page_title="Pokémon Info", page_icon="🐉")

st.markdown("# 🐉 Pokémon Info")
st.sidebar.header("Pokémon Info")
st.write(
    """This page fetches Pokémon information from the [PokéAPI](https://pokeapi.co/)."""
)

name = st.text_input("Enter Pokémon Name", "pikachu").lower()

if st.button("Get Pokémon"):
    if name:
        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
            if response.status_code == 200:
                data = response.json()
                
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.image(data["sprites"]["front_default"], width=200)
                
                with col2:
                    st.subheader(data["name"].capitalize())
                    st.write(f"**Height:** {data['height']}")
                    st.write(f"**Weight:** {data['weight']}")
                    types = [t["type"]["name"] for t in data["types"]]
                    st.write(f"**Types:** {', '.join(types)}")
            else:
                st.error("Pokémon not found. Please check the spelling.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a Pokémon name.")
