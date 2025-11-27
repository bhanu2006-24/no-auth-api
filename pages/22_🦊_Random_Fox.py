import streamlit as st
import requests

st.set_page_config(page_title="Random Fox", page_icon="🦊")

st.markdown("# 🦊 Random Fox")
st.sidebar.header("Random Fox")
st.write(
    """This page fetches a random fox image from the [Random Fox API](https://randomfox.ca/)."""
)

if st.button("Get Fox"):
    try:
        response = requests.get("https://randomfox.ca/floof/")
        if response.status_code == 200:
            data = response.json()
            st.image(data["image"], caption="What does the fox say?", use_column_width=True)
        else:
            st.error("Failed to fetch fox. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
