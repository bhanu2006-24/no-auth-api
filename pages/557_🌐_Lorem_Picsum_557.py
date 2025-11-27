import streamlit as st

st.set_page_config(page_title="Lorem Picsum", page_icon="🖼️")
st.markdown("# 🖼️ Lorem Picsum")

if st.button("Get Random Image"):
    st.image("https://picsum.photos/800/600")
