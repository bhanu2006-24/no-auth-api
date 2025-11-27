import streamlit as st
import requests

st.set_page_config(page_title="xColors", page_icon="🎨")

st.markdown("# 🎨 xColors Random Color")
st.write("Get a random color.")

if st.button("Get Color"):
    try:
        response = requests.get("https://x-colors.yurace.pro/api/random")
        if response.status_code == 200:
            data = response.json()
            hex_code = data["hex"]
            rgb = data["rgb"]
            
            st.color_picker("Color", hex_code, disabled=True)
            st.write(f"**HEX:** {hex_code}")
            st.write(f"**RGB:** {rgb}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
