import streamlit as st
import requests

st.set_page_config(page_title="Chronicling America", page_icon="📰")
st.markdown("# 📰 Chronicling America")

term = st.text_input("Search Term", "aviation")

if st.button("Search"):
    try:
        response = requests.get(f"https://chroniclingamerica.loc.gov/search/pages/results/?andtext={term}&format=json")
        if response.status_code == 200:
            data = response.json()
            st.write(f"Total Results: {data['totalItems']}")
            for item in data['items'][:3]:
                st.subheader(item['title'])
                st.write(f"**Date:** {item['date']}")
                st.markdown(f"[View Page](https://chroniclingamerica.loc.gov{item['id']})")
    except Exception as e:
        st.error(f"Error: {e}")
