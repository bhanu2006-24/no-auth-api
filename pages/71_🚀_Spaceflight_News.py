import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Spaceflight News", page_icon="🚀")

st.title("🚀 Spaceflight News")
st.markdown("Get the latest spaceflight news using [Spaceflight News API](https://www.spaceflightnewsapi.net/).")

if st.button("Get Latest News"):
    try:
        response = requests.get("https://api.spaceflightnewsapi.net/v3/articles?_limit=10")
        if response.status_code == 200:
            articles = response.json()
            for article in articles:
                with st.expander(article['title']):
                    st.image(article['imageUrl'], use_column_width=True)
                    st.write(f"**Published:** {article['publishedAt']}")
                    st.write(f"**Source:** {article['newsSite']}")
                    st.write(article['summary'])
                    st.markdown(f"[Read Full Article]({article['url']})")
        else:
            st.error("Failed to fetch news.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
