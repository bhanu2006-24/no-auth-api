import streamlit as st
import requests

st.set_page_config(page_title="Nationalize.io", page_icon="🇺🇳")

st.markdown("# 🇺🇳 Nationalize.io")
st.write("Predict nationality from name.")

name = st.text_input("Name", "Michael")

if st.button("Predict"):
    try:
        response = requests.get(f"https://api.nationalize.io?name={name}")
        if response.status_code == 200:
            data = response.json()
            for country in data['country']:
                st.write(f"**{country['country_id']}:** {country['probability']:.0%}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
