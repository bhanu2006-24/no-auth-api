import streamlit as st
import requests
import xml.etree.ElementTree as ET

st.set_page_config(page_title="Bank of Russia", page_icon="🇷🇺")

st.markdown("# 🇷🇺 Bank of Russia")
st.write("Exchange rates.")

if st.button("Get Rates"):
    try:
        # Getting today's rates
        import datetime
        today = datetime.date.today().strftime("%d/%m/%Y")
        response = requests.get(f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={today}")
        if response.status_code == 200:
            # Parse XML
            root = ET.fromstring(response.content)
            for valute in root.findall('Valute')[:5]: # Show first 5
                name = valute.find('Name').text
                value = valute.find('Value').text
                st.write(f"**{name}:** {value} RUB")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
