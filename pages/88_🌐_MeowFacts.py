import streamlit as st
import requests

st.set_page_config(page_title="MeowFacts", page_icon="🐈")

st.markdown("# 🐈 MeowFacts")
st.write("Random facts about cats.")

if st.button("🐈 Get Fact"):
    try:
        response = requests.get("https://meowfacts.herokuapp.com/")
        if response.status_code == 200:
            data = response.json()
            st.success(data["data"][0])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
