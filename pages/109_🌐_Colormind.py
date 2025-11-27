import streamlit as st
import requests
import json

st.set_page_config(page_title="Colormind", page_icon="🌈")

st.markdown("# 🌈 Colormind Palette Generator")
st.write("Generate AI-powered color palettes.")

if st.button("Generate Palette"):
    try:
        response = requests.post("http://colormind.io/api/", data=json.dumps({"model": "default"}))
        if response.status_code == 200:
            data = response.json()
            palette = data["result"]
            
            cols = st.columns(5)
            for i, color in enumerate(palette):
                hex_color = '#{:02x}{:02x}{:02x}'.format(*color)
                with cols[i]:
                    st.color_picker(f"Color {i+1}", hex_color, disabled=True)
                    st.write(hex_color)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
