import streamlit as st
import requests

st.set_page_config(page_title="Shibe Online", page_icon="🐕")

st.markdown("# 🐕 Shibe Online")
st.write("Cute Shiba Inu pictures.")

count = st.slider("How many Shibes?", 1, 10, 1)

if st.button("Get Shibes"):
    try:
        response = requests.get(f"http://shibe.online/api/shibes?count={count}")
        if response.status_code == 200:
            urls = response.json()
            for url in urls:
                st.image(url, use_column_width=True)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
