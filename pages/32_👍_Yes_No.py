import streamlit as st
import requests

st.set_page_config(page_title="Yes/No", page_icon="👍")

st.markdown("# 👍 Yes/No Decision")
st.sidebar.header("Yes/No")
st.write(
    """This page randomly decides Yes or No using the [YesNo API](https://yesno.wtf/)."""
)

if st.button("Decide for me"):
    try:
        response = requests.get("https://yesno.wtf/api")
        if response.status_code == 200:
            data = response.json()
            st.header(data["answer"].upper())
            st.image(data["image"], use_column_width=True)
        else:
            st.error("Failed to fetch decision. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
