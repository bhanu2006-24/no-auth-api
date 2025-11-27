import streamlit as st
import requests

st.set_page_config(page_title="Digimon Info", page_icon="👾")
st.markdown("# 👾 Digimon Information")

name = st.text_input("Digimon Name", "Agumon")

if st.button("Search"):
    try:
        response = requests.get(f"https://digi-api.com/api/v1/digimon/{name}")
        if response.status_code == 200:
            data = response.json()
            st.header(data['name'])
            st.image(data['images'][0]['href'])
            st.write("Types:")
            for t in data['types']:
                st.write(f"- {t['type']}")
        else:
            st.error("Digimon not found.")
    except Exception as e:
        st.error(f"Error: {e}")
