import streamlit as st
import requests

st.set_page_config(page_title="HTTP Cats", page_icon="🐱")

st.markdown("# 🐱 HTTP Cats")
st.sidebar.header("HTTP Cats")
st.write(
    """This page displays HTTP status codes as cats using the [HTTP Cat API](https://http.cat/)."""
)

status_code = st.number_input("Enter HTTP Status Code", value=404, step=1)

if st.button("Get Cat"):
    url = f"https://http.cat/{status_code}"
    # Check if image exists by making a HEAD request
    try:
        response = requests.head(url)
        if response.status_code == 200:
            st.image(url, caption=f"Status Code {status_code}", use_column_width=True)
        else:
            st.error("Cat not found for this status code.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
