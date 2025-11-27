import streamlit as st
import requests
import datetime

st.set_page_config(page_title="Russian Calendar", page_icon="🇷🇺")

st.markdown("# 🇷🇺 Russian Calendar")
st.write("Check for Russian holidays and non-working days.")

year = st.number_input("Year", 2020, 2030, datetime.datetime.now().year)

if st.button("Get Calendar"):
    try:
        response = requests.get(f"https://isdayoff.ru/api/getdata?year={year}&cc=ru&pre=1&delimeter=%0A")
        if response.status_code == 200:
            # The API returns a string of 0s and 1s for each day
            data = response.text
            st.success("Data fetched successfully.")
            st.write(f"Data length: {len(data)} days")
            st.info("0 = Working Day, 1 = Non-working Day")
            
            # Simple visualizer for first month
            st.write("### January Preview")
            days = list(data[:31])
            cols = st.columns(7)
            for i, day in enumerate(days):
                with cols[i % 7]:
                    color = "red" if day == '1' else "green"
                    st.markdown(f":{color}[{i+1}]")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
