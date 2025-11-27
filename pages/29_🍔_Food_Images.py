import streamlit as st
import requests

st.set_page_config(page_title="Food Images", page_icon="🍔")

st.markdown("# 🍔 Food Images")
st.sidebar.header("Food Images")
st.write(
    """This page fetches a random food image using the [Foodish API](https://foodish-api.com/)."""
)

if st.button("Get Food"):
    try:
        response = requests.get("https://foodish-api.com/api/")
        if response.status_code == 200:
            data = response.json()
            st.image(data["image"], caption="Yummy!", use_column_width=True)
        else:
            st.error("Failed to fetch food. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
