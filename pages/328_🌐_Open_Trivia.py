import streamlit as st
import requests
import html

st.set_page_config(page_title="Open Trivia", page_icon="❓")
st.markdown("# ❓ Open Trivia DB")

if st.button("Get Question"):
    try:
        response = requests.get("https://opentdb.com/api.php?amount=1")
        if response.status_code == 200:
            data = response.json()['results'][0]
            st.write(f"**Category:** {data['category']}")
            st.write(f"**Difficulty:** {data['difficulty']}")
            st.write(f"**Question:** {html.unescape(data['question'])}")
            with st.expander("Answer"):
                st.write(data['correct_answer'])
    except Exception as e:
        st.error(f"Error: {e}")
