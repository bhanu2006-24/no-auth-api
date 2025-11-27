import streamlit as st
import requests

st.set_page_config(page_title="IPinfo", page_icon="🌍")

st.markdown("# 🌍 IPinfo")
st.write("IP geolocation.")

ip = st.text_input("IP Address (Leave empty for yours)", "")

if st.button("Get Info"):
    try:
        url = f"https://ipinfo.io/{ip}/json" if ip else "https://ipinfo.io/json"
        response = requests.get(url)
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
