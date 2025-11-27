import streamlit as st
import requests

st.set_page_config(page_title="Tenders Hungary", page_icon="🇭🇺")

st.markdown("# 🇭🇺 Tenders in Hungary")
st.write("Latest government tenders.")

if st.button("Fetch Tenders"):
    try:
        response = requests.get("https://tenders.guru/api/hu/tenders")
        if response.status_code == 200:
            data = response.json()
            for tender in data['data'][:5]:
                st.subheader(tender['title'])
                st.write(f"**Date:** {tender['date']}")
                st.write(f"**Category:** {tender['category_name']}")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
