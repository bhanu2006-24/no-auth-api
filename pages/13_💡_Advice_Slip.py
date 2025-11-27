import streamlit as st
import requests

st.set_page_config(page_title="Advice Slip", page_icon="💡")

st.markdown("# 💡 Advice Slip")
st.sidebar.header("Advice Slip")
st.write(
    """This page fetches a random piece of advice from the [Advice Slip API](https://api.adviceslip.com/)."""
)

if st.button("Get Advice"):
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        if response.status_code == 200:
            data = response.json()
            st.success(data["slip"]["advice"])
        else:
            st.error("Failed to fetch advice. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
