import streamlit as st
import requests
import xml.etree.ElementTree as ET

st.set_page_config(page_title="BoardGameGeek", page_icon="🎲")

st.markdown("# 🎲 BoardGameGeek")

if st.button("Get Hot Games"):
    try:
        response = requests.get("https://boardgamegeek.com/xmlapi2/hot?type=boardgame")
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            for item in root.findall('item')[:5]:
                name = item.find('name').get('value')
                year = item.find('yearpublished').get('value')
                st.write(f"**{name}** ({year})")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
