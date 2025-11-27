import streamlit as st
import requests

st.set_page_config(page_title="Quotable", page_icon="💬")

st.markdown("# 💬 Quotable")
st.sidebar.header("Quotable")
st.write(
    """This page fetches famous quotes using the [Quotable API](https://github.com/lukePeavey/quotable)."""
)

if st.button("Get Quote"):
    try:
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            data = response.json()
            st.markdown(f"### *\"{data['content']}\"*")
            st.caption(f"- {data['author']}")
            st.write(f"**Tags:** {', '.join(data['tags'])}")
        else:
            st.error("Failed to fetch quote. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
