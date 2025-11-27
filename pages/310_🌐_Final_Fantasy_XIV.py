import streamlit as st
import requests

st.set_page_config(page_title="FFXIV API", page_icon="⚔️")
st.markdown("# ⚔️ Final Fantasy XIV")

if st.button("Search Item"):
    st.info("Use XIVAPI.com directly for complex queries.")
