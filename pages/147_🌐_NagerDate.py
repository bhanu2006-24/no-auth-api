import streamlit as st
import requests
import datetime

st.set_page_config(page_title="Nager.Date", page_icon="📅")

st.markdown("# 📅 Public Holidays")
st.write("Global public holidays.")

country = st.text_input("Country Code (e.g., US, GB, AT)", "US")
year = st.number_input("Year", 2020, 2030, datetime.datetime.now().year)

if st.button("Get Holidays"):
    try:
        response = requests.get(f"https://date.nager.at/api/v3/publicholidays/{year}/{country}")
        if response.status_code == 200:
            holidays = response.json()
            for holiday in holidays:
                st.write(f"**{holiday['date']}:** {holiday['name']} ({holiday['localName']})")
        else:
            st.error("API Error (Invalid Country Code?)")
    except Exception as e:
        st.error(f"Error: {e}")
