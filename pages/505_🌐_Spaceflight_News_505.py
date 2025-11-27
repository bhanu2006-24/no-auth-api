import streamlit as st
import requests

st.set_page_config(page_title="Spaceflight News", page_icon="🚀")
st.markdown("# 🚀 Spaceflight News")

if st.button("Get Latest News"):
    try:
        response = requests.get("https://api.spaceflightnewsapi.net/v4/articles/?limit=5")
        if response.status_code == 200:
            data = response.json()
            for article in data['results']:
                st.subheader(article['title'])
                st.image(article['image_url'])
                st.write(article['summary'])
                st.markdown(f"[Read More]({article['url']})")
                st.markdown("---")
    except Exception as e:
        st.error(f"Error: {e}")
