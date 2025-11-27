import streamlit as st
import requests

st.set_page_config(page_title="CheapShark", page_icon="🦈")

st.markdown("# 🦈 CheapShark")
st.write("Game deals.")

title = st.text_input("Game Title", "Batman")

if st.button("Search Deals"):
    try:
        response = requests.get(f"https://www.cheapshark.com/api/1.0/games?title={title}&limit=5")
        if response.status_code == 200:
            data = response.json()
            for game in data:
                st.subheader(game['external'])
                st.write(f"**Cheapest:** ${game['cheapest']}")
                st.image(game['thumb'], width=100)
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
