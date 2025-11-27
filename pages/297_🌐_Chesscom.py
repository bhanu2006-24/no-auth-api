import streamlit as st
import requests

st.set_page_config(page_title="Chess.com", page_icon="♟️")

st.markdown("# ♟️ Chess.com")

username = st.text_input("Username", "hikaru")

if st.button("Get Stats"):
    try:
        response = requests.get(f"https://api.chess.com/pub/player/{username}/stats")
        if response.status_code == 200:
            data = response.json()
            if 'chess_blitz' in data:
                st.metric("Blitz Rating", data['chess_blitz']['last']['rating'])
            if 'chess_rapid' in data:
                st.metric("Rapid Rating", data['chess_rapid']['last']['rating'])
        else:
            st.error("User not found.")
    except Exception as e:
        st.error(f"Error: {e}")
