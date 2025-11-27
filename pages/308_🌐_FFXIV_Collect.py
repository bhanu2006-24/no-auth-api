import streamlit as st
import requests

st.set_page_config(page_title="FFXIV Collect", page_icon="⚔️")
st.markdown("# ⚔️ FFXIV Collect")

if st.button("Get Latest Mounts"):
    try:
        response = requests.get("https://ffxivcollect.com/api/mounts")
        if response.status_code == 200:
            data = response.json()
            for mount in data['results'][:5]:
                st.subheader(mount['name'])
                st.image(mount['image'])
                st.write(mount['description'])
    except Exception as e:
        st.error(f"Error: {e}")
