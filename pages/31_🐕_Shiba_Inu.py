import streamlit as st
import requests

st.set_page_config(page_title="Shiba Inu", page_icon="🐕")

st.markdown("# 🐕 Shiba Inu Images")
st.sidebar.header("Shiba Inu")
st.write(
    """This page fetches a random Shiba Inu image using the [Shibe.online API](https://shibe.online/)."""
)

if st.button("Get Shiba"):
    try:
        response = requests.get("https://shibe.online/api/shibes?count=1")
        if response.status_code == 200:
            data = response.json()
            st.image(data[0], caption="Such wow!", use_column_width=True)
        else:
            st.error("Failed to fetch Shiba. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
