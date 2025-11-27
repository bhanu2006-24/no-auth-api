import streamlit as st
import requests

st.set_page_config(page_title="Cloudflare Trace", page_icon="☁️")

st.markdown("# ☁️ Cloudflare Trace")
st.write("Get your connection info.")

if st.button("Trace"):
    try:
        response = requests.get("https://www.cloudflare.com/cdn-cgi/trace")
        if response.status_code == 200:
            st.text(response.text)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
