import streamlit as st
import requests

st.set_page_config(page_title="Amiibo API", page_icon="🎮")

st.markdown("# 🎮 Amiibo API")

name = st.text_input("Character Name", "Mario")

if st.button("Search"):
    try:
        response = requests.get(f"https://www.amiiboapi.com/api/amiibo/?name={name}")
        if response.status_code == 200:
            data = response.json()
            for amiibo in data['amiibo'][:5]:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(amiibo['image'])
                with col2:
                    st.subheader(amiibo['name'])
                    st.write(f"**Series:** {amiibo['amiiboSeries']}")
                    st.write(f"**Game:** {amiibo['gameSeries']}")
        else:
            st.error("Not Found.")
    except Exception as e:
        st.error(f"Error: {e}")
