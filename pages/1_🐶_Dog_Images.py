import streamlit as st
import requests

st.set_page_config(page_title="Dog Images", page_icon="🐶")

st.markdown("# 🐶 Random Dog Images")
st.sidebar.header("Dog Images")
st.write(
    """This page fetches a random dog image from the [Dog CEO API](https://dog.ceo/dog-api/)."""
)

if st.button("Get New Dog"):
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        if response.status_code == 200:
            data = response.json()
            image_url = data["message"]
            st.image(image_url, caption="A Random Doggo", use_column_width=True)
        else:
            st.error("Failed to fetch image. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
