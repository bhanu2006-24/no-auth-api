import streamlit as st
import requests

st.set_page_config(page_title="REST Countries", page_icon="🏳️")
st.markdown("# 🏳️ REST Countries")

name = st.text_input("Country Name", "France")

if st.button("Get Info"):
    try:
        response = requests.get(f"https://restcountries.com/v3.1/name/{name}")
        if response.status_code == 200:
            data = response.json()[0]
            st.header(data['name']['common'])
            st.image(data['flags']['png'])
            st.write(f"**Capital:** {', '.join(data.get('capital', []))}")
            st.write(f"**Population:** {data['population']:,}")
    except Exception as e:
        st.error(f"Error: {e}")
