import streamlit as st
import requests

st.set_page_config(page_title="jsDelivr", page_icon="📦")

st.markdown("# 📦 jsDelivr")
st.write("CDN for open source.")

package = st.text_input("NPM Package", "jquery")

if st.button("Get Info"):
    try:
        response = requests.get(f"https://data.jsdelivr.com/v1/package/npm/{package}")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Package not found.")
    except Exception as e:
        st.error(f"Error: {e}")
