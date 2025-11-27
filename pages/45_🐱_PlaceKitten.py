import streamlit as st

st.set_page_config(page_title="PlaceKitten", page_icon="🐱")

st.markdown("# 🐱 PlaceKitten")
st.sidebar.header("PlaceKitten")
st.write(
    """This page generates placeholder kitten images using [PlaceKitten](https://placekitten.com/)."""
)

width = st.slider("Width", 100, 800, 400)
height = st.slider("Height", 100, 800, 300)

if st.button("Get Kitten"):
    url = f"https://placekitten.com/{width}/{height}"
    st.image(url, caption=f"Kitten ({width}x{height})")
