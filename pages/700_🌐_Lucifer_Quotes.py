import streamlit as st
import requests

st.set_page_config(page_title="Lucifer Quotes", page_icon="😈")
st.markdown("# 😈 Lucifer Quotes")

if st.button("Get Quote"):
    try:
        response = requests.get("https://lucifer-quotes.vercel.app/api/quotes")
        if response.status_code == 200:
            data = response.json()
            data = data[0]
            st.write(f"**{data["quote"]}**")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
