import streamlit as st
import requests
import base64
import zlib

st.set_page_config(page_title="Kroki", page_icon="🖍️")

st.markdown("# 🖍️ Kroki Diagram")
st.write("Text to diagram.")

diagram_type = st.selectbox("Type", ["graphviz", "mermaid", "plantuml"])
source = st.text_area("Source Code", 'digraph G { Hello -> World }' if diagram_type == "graphviz" else 'graph TD; A-->B;')

if st.button("Render"):
    try:
        # Kroki expects base64 encoded deflated data for GET, or raw POST
        # Using POST for simplicity
        response = requests.post(f"https://kroki.io/{diagram_type}/svg", data=source)
        if response.status_code == 200:
            st.image(response.content, format="svg")
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"Error: {e}")
