import streamlit as st
import requests

st.set_page_config(page_title="Catboy", page_icon="😸")

st.markdown("# 😸 Catboy Images")
st.sidebar.header("Catboy")
st.write("Random images of Catboys.")

if st.button("Get Catboy"):
    try:
        response = requests.get("https://api.catboys.com/img")
        if response.status_code == 200:
            data = response.json()
            st.image(data["url"], caption=f"Artist: {data.get('artist', 'Unknown')}", use_column_width=True)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
