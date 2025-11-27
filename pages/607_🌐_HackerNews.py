import streamlit as st
import requests

st.set_page_config(page_title="Hacker News", page_icon="📰")
st.markdown("# 📰 Hacker News")

if st.button("Top Stories"):
    try:
        # Get top 5 IDs
        ids_response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
        if ids_response.status_code == 200:
            ids = ids_response.json()[:5]
            for id in ids:
                item_response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json")
                if item_response.status_code == 200:
                    item = item_response.json()
                    st.subheader(item.get('title', 'No Title'))
                    st.write(f"**Score:** {item.get('score', 0)} | **By:** {item.get('by', 'Unknown')}")
                    if 'url' in item:
                        st.markdown(f"[Link]({item['url']})")
                    st.markdown("---")
    except Exception as e:
        st.error(f"Error: {e}")
