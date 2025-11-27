import streamlit as st
import requests

st.set_page_config(page_title="UUID Generator", page_icon="🆔")

st.title("🆔 UUID Generator")
st.markdown("Generate UUIDs (Universally Unique Identifiers) using [UUID Tools](https://www.uuidtools.com/).")

count = st.slider("Number of UUIDs to generate", 1, 10, 5)

if st.button("Generate UUIDs"):
    try:
        response = requests.get(f"https://www.uuidtools.com/api/generate/v1/count/{count}")
        if response.status_code == 200:
            uuids = response.json()
            st.write("### Generated UUIDs:")
            for uuid in uuids:
                st.code(uuid, language="text")
        else:
            st.error("Failed to fetch UUIDs.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
