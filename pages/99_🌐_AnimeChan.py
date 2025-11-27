import streamlit as st
import requests

st.set_page_config(page_title="AnimeChan", page_icon="👺")

st.markdown("# 👺 Anime Quotes")

if st.button("Get Random Quote"):
    try:
        response = requests.get("https://api.animechan.io/v1/quotes/random")
        if response.status_code == 200:
            data = response.json()
            st.markdown(f"### "{data['data']['content']}"")
            st.markdown(f"**— {data['data']['character']}** *({data['data']['anime']['name']})*")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
