import streamlit as st
import requests
import datetime

st.set_page_config(page_title="Czech Namedays", page_icon="🇨🇿")

st.markdown("# 🇨🇿 Czech Namedays")
st.write("Find out who has a nameday today in Czechia.")

if st.button("Get Nameday"):
    try:
        today = datetime.date.today()
        response = requests.get(f"https://svatky.adresa.info/json?date={today.strftime('%d%m')}")
        if response.status_code == 200:
            data = response.json()
            # API returns list of entries
            names = [entry['name'] for entry in data]
            st.success(f"Today's Nameday: {', '.join(names)}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
