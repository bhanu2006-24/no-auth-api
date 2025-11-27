import streamlit as st
import requests

st.set_page_config(page_title="RSS to JSON", page_icon="📰")

st.markdown("# 📰 RSS to JSON")

url = st.text_input("RSS Feed URL", "https://feeds.bbci.co.uk/news/rss.xml")

if st.button("Convert"):
    try:
        response = requests.get(f"https://api.rss2json.com/v1/api.json?rss_url={url}")
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'ok':
                st.subheader(data['feed']['title'])
                for item in data['items'][:5]:
                    st.write(f"**{item['title']}**")
                    st.caption(item['pubDate'])
                    st.markdown("---")
            else:
                st.error("Conversion failed.")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
