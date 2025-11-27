import streamlit as st
import requests

st.set_page_config(page_title="Useless Facts", page_icon="🧠")

st.markdown("# 🧠 Useless Facts")
st.sidebar.header("Useless Facts")
st.write(
    """This page fetches a random useless fact from the [Useless Facts API](https://uselessfacts.jsph.pl/)."""
)

if st.button("Get Useless Fact"):
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        if response.status_code == 200:
            data = response.json()
            st.info(data["text"])
        else:
            st.error("Failed to fetch fact. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
