import streamlit as st
import requests

st.set_page_config(page_title="Kanye Quotes", page_icon="🎤")

st.markdown("# 🎤 Kanye Quotes")
st.sidebar.header("Kanye Quotes")
st.write(
    """This page fetches a random quote from Kanye West using the [Kanye.rest API](https://kanye.rest/)."""
)

if st.button("Get Quote"):
    try:
        response = requests.get("https://api.kanye.rest/")
        if response.status_code == 200:
            data = response.json()
            st.markdown(f"### *\"{data['quote']}\"*")
            st.caption("- Kanye West")
        else:
            st.error("Failed to fetch quote. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
