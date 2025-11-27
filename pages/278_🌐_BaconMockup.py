import streamlit as st

st.set_page_config(page_title="BaconMockup", page_icon="🥓")

st.markdown("# 🥓 BaconMockup")
st.write("Meaty placeholders.")

width = st.slider("Width", 100, 500, 300)
height = st.slider("Height", 100, 500, 200)

if st.button("Get Bacon"):
    url = f"https://baconmockup.com/{width}/{height}"
    st.image(url)
