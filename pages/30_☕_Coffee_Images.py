import streamlit as st
import requests

st.set_page_config(page_title="Coffee Images", page_icon="☕")

st.markdown("# ☕ Coffee Images")
st.sidebar.header("Coffee Images")
st.write(
    """This page fetches a random coffee image using the [Coffee API](https://coffee.alexflipnote.dev/)."""
)

if st.button("Get Coffee"):
    try:
        response = requests.get("https://coffee.alexflipnote.dev/random.json")
        if response.status_code == 200:
            data = response.json()
            st.image(data["file"], caption="Coffee Time!", use_column_width=True)
        else:
            st.error("Failed to fetch coffee. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
