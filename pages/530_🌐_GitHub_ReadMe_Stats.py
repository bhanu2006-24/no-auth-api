import streamlit as st

st.set_page_config(page_title="GitHub Stats", page_icon="📊")
st.markdown("# 📊 GitHub ReadMe Stats")

username = st.text_input("GitHub Username", "anuraghazra")

if st.button("Generate Card"):
    url = f"https://github-readme-stats.vercel.app/api?username={username}&show_icons=true&theme=radical"
    st.image(url)
