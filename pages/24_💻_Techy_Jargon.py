import streamlit as st
import requests

st.set_page_config(page_title="Techy Jargon", page_icon="💻")

st.markdown("# 💻 Techy Jargon")
st.sidebar.header("Techy Jargon")
st.write(
    """This page generates random tech jargon using the [Techy API](https://techy-api.vercel.app/)."""
)

if st.button("Generate Jargon"):
    try:
        response = requests.get("https://techy-api.vercel.app/api/json")
        if response.status_code == 200:
            data = response.json()
            st.success(data["message"])
        else:
            st.error("Failed to fetch jargon. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
