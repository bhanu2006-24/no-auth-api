import streamlit as st
import requests

st.set_page_config(page_title="SWAPI", page_icon="🌌")
st.markdown("# 🌌 Star Wars API")

if st.button("Get Random Person"):
    try:
        import random
        id = random.randint(1, 80)
        response = requests.get(f"https://swapi.dev/api/people/{id}/")
        if response.status_code == 200:
            data = response.json()
            st.header(data['name'])
            st.write(f"**Height:** {data['height']}")
            st.write(f"**Mass:** {data['mass']}")
            st.write(f"**Gender:** {data['gender']}")
    except Exception as e:
        st.error(f"Error: {e}")
