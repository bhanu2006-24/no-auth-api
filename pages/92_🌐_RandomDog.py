import streamlit as st
import requests

st.set_page_config(page_title="Random Dog", page_icon="🐕‍🦺")

st.markdown("# 🐕‍🦺 Random Dog")

if st.button("Fetch Dog"):
    try:
        response = requests.get("https://random.dog/woof.json")
        if response.status_code == 200:
            data = response.json()
            url = data["url"]
            if url.endswith(".mp4") or url.endswith(".webm"):
                st.video(url)
            else:
                st.image(url, use_column_width=True)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
