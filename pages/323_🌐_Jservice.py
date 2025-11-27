import streamlit as st
import requests

st.set_page_config(page_title="JService", page_icon="🧠")
st.markdown("# 🧠 JService (Jeopardy)")

if st.button("Get Question"):
    try:
        response = requests.get("https://jservice.io/api/random")
        if response.status_code == 200:
            data = response.json()[0]
            st.write(f"**Category:** {data['category']['title']}")
            st.write(f"**Question:** {data['question']}")
            with st.expander("Show Answer"):
                st.write(data['answer'])
    except Exception as e:
        st.error(f"Error: {e}")
