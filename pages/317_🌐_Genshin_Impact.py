import streamlit as st
import requests

st.set_page_config(page_title="Genshin Impact", page_icon="✨")
st.markdown("# ✨ Genshin Impact")

if st.button("Get Characters"):
    try:
        response = requests.get("https://genshin.jmp.blue/characters")
        if response.status_code == 200:
            data = response.json()
            st.write(f"Total Characters: {len(data)}")
            st.write(", ".join(data))
    except Exception as e:
        st.error(f"Error: {e}")
