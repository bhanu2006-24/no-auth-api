import streamlit as st

st.set_page_config(page_title="Icon Horse", page_icon="🐴")

st.markdown("# 🐴 Icon Horse")
st.write("Get the favicon for any website.")

domain = st.text_input("Enter Domain (e.g., google.com)", "google.com")

if st.button("Get Icon"):
    url = f"https://icon.horse/icon/{domain}"
    st.image(url, caption=f"Icon for {domain}")
    st.code(url)
