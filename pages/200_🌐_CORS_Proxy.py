import streamlit as st

st.set_page_config(page_title="CORS Proxy", page_icon="🔄")

st.markdown("# 🔄 CORS Proxy")
st.write("Test CORS proxies.")

url = st.text_input("URL to fetch via Proxy", "https://google.com")

if st.button("Fetch"):
    st.info("Public CORS proxies are often unstable. We recommend setting up your own.")
