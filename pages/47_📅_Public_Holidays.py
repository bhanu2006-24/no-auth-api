import streamlit as st
import requests
import datetime

st.set_page_config(page_title="Public Holidays", page_icon="📅")

st.markdown("# 📅 Public Holidays")
st.sidebar.header("Public Holidays")
st.write(
    """This page fetches upcoming public holidays for a country using the [Nager.Date API](https://date.nager.at/)."""
)

country_code = st.text_input("Enter Country Code (e.g., US, GB, DE)", "US").upper()

if st.button("Get Holidays"):
    if country_code:
        try:
            response = requests.get(f"https://date.nager.at/api/v3/NextPublicHolidays/{country_code}")
            if response.status_code == 200:
                data = response.json()
                if data:
                    st.success(f"Upcoming holidays in {country_code}:")
                    for holiday in data:
                        date = holiday["date"]
                        name = holiday["name"]
                        local_name = holiday.get("localName", "")
                        st.write(f"**{date}:** {name} ({local_name})")
                else:
                    st.warning("No upcoming holidays found.")
            else:
                st.error("Failed to fetch holidays. Check the country code or try again later.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a country code.")
