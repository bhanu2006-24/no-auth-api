import streamlit as st

st.set_page_config(page_title="PlaceDog", page_icon="🐩")

st.markdown("# 🐩 PlaceDog")
st.write("Generate placeholder dog images.")

col1, col2 = st.columns(2)
with col1:
    width = st.slider("Width", 100, 1000, 500)
with col2:
    height = st.slider("Height", 100, 1000, 400)

if st.button("Generate Dog"):
    url = f"https://placedog.net/{width}/{height}"
    st.image(url, caption=f"Dog {width}x{height}")
    st.code(url)
