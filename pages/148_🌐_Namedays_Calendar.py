import streamlit as st
import requests

st.set_page_config(page_title="Namedays", page_icon="🎉")

st.markdown("# 🎉 Namedays")
st.write("Find namedays for different countries.")

country = st.selectbox("Country", ["us", "cz", "sk", "pl", "fr", "hu", "hr", "se", "at", "it", "es", "de"])
day = st.number_input("Day", 1, 31, 1)
month = st.number_input("Month", 1, 12, 1)

if st.button("Check Nameday"):
    try:
        response = requests.get(f"https://api.abalin.net/namedays?country={country}&day={day}&month={month}")
        if response.status_code == 200:
            data = response.json()
            names = data.get("data", {}).get("namedays", {}).get(country)
            st.success(f"Nameday in {country.upper()}: {names}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
