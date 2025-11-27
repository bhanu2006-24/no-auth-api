import streamlit as st
import requests

st.set_page_config(page_title="D&D 5e", page_icon="🐉")
st.markdown("# 🐉 Dungeons & Dragons 5e")

category = st.selectbox("Category", ["spells", "monsters", "classes"])

if st.button("List Items"):
    try:
        response = requests.get(f"https://www.dnd5eapi.co/api/{category}")
        if response.status_code == 200:
            data = response.json()
            st.write(f"Total: {data['count']}")
            st.json(data['results'][:10])
    except Exception as e:
        st.error(f"Error: {e}")
