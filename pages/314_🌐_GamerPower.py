import streamlit as st
import requests

st.set_page_config(page_title="GamerPower", page_icon="🎮")
st.markdown("# 🎮 GamerPower")
st.write("Game giveaways.")

if st.button("Get Giveaways"):
    try:
        response = requests.get("https://www.gamerpower.com/api/giveaways")
        if response.status_code == 200:
            data = response.json()
            for item in data[:5]:
                st.subheader(item['title'])
                st.image(item['image'])
                st.write(item['description'])
                st.markdown(f"[Get it]({item['open_giveaway_url']})")
    except Exception as e:
        st.error(f"Error: {e}")
