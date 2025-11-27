import streamlit as st
import requests

st.set_page_config(page_title="Random Duck", page_icon="🦆")

st.markdown("# 🦆 Random Duck")
st.sidebar.header("Random Duck")
st.write(
    """This page fetches a random duck image from the [Random Duck API](https://random-d.uk/)."""
)

if st.button("Get Duck"):
    try:
        response = requests.get("https://random-d.uk/api/v2/random")
        if response.status_code == 200:
            data = response.json()
            st.image(data["url"], caption="Quack!", use_column_width=True)
        else:
            st.error("Failed to fetch duck. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
