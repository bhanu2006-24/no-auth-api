import streamlit as st
import requests

st.set_page_config(page_title="Hyrule Compendium", page_icon="🛡️")
st.markdown("# 🛡️ Hyrule Compendium")

if st.button("Get Random Entry"):
    try:
        response = requests.get("https://botw-compendium.herokuapp.com/api/v2/entry/random")
        if response.status_code == 200:
            data = response.json()['data']
            st.header(data['name'])
            st.image(data['image'])
            st.write(data['description'])
    except Exception as e:
        st.error(f"Error: {e}")
