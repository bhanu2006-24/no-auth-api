import streamlit as st
import requests

st.set_page_config(page_title="MHW", page_icon="🦖")
st.markdown("# 🦖 Monster Hunter World")

if st.button("Get Monsters"):
    try:
        response = requests.get("https://mhw-db.com/monsters")
        if response.status_code == 200:
            data = response.json()
            for monster in data[:5]:
                st.subheader(monster['name'])
                st.write(f"**Type:** {monster['type']}")
                st.write(f"**Species:** {monster['species']}")
    except Exception as e:
        st.error(f"Error: {e}")
