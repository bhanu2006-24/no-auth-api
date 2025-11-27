import streamlit as st
import requests

st.set_page_config(page_title="NBA Stats", page_icon="🏀")
st.markdown("# 🏀 NBA Stats (balldontlie)")

player = st.text_input("Player Name", "LeBron James")

if st.button("Search"):
    try:
        response = requests.get(f"https://www.balldontlie.io/api/v1/players?search={player}")
        if response.status_code == 200:
            data = response.json()
            for p in data['data']:
                st.subheader(f"{p['first_name']} {p['last_name']}")
                st.write(f"**Team:** {p['team']['full_name']}")
                st.write(f"**Position:** {p['position']}")
    except Exception as e:
        st.error(f"Error: {e}")
