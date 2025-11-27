import streamlit as st
import requests

st.set_page_config(page_title="Excuser", page_icon="🤥")

st.markdown("# 🤥 Excuser")
st.sidebar.header("Excuser")
st.write(
    """This page generates random excuses using the [Excuser API](https://excuser-three.vercel.app/)."""
)

category = st.selectbox("Category", ["family", "office", "children", "college", "party"])

if st.button("Get Excuse"):
    try:
        response = requests.get(f"https://excuser-three.vercel.app/v1/excuse/{category}")
        if response.status_code == 200:
            data = response.json()
            st.success(data[0]["excuse"])
        else:
            st.error("Failed to fetch excuse. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
