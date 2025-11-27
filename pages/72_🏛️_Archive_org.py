import streamlit as st
import requests

st.set_page_config(page_title="Internet Archive", page_icon="🏛️")

st.title("🏛️ Internet Archive Search")
st.markdown("Search the Internet Archive using [Archive.org API](https://archive.org/).")

query = st.text_input("Search Query", "NASA")

if st.button("Search"):
    if query:
        try:
            # Using the advanced search API
            url = "https://archive.org/advancedsearch.php"
            params = {
                'q': query,
                'fl[]': ['identifier', 'title', 'creator', 'date'],
                'sort[]': '',
                'rows': '10',
                'page': '1',
                'output': 'json'
            }
            response = requests.get(url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                docs = data['response']['docs']
                
                if docs:
                    for doc in docs:
                        title = doc.get('title', 'Unknown Title')
                        identifier = doc.get('identifier', '')
                        creator = doc.get('creator', 'Unknown Creator')
                        date = doc.get('date', 'Unknown Date')
                        
                        st.subheader(title)
                        st.write(f"**Creator:** {creator}")
                        st.write(f"**Date:** {date}")
                        st.markdown(f"[View on Archive.org](https://archive.org/details/{identifier})")
                        st.markdown("---")
                else:
                    st.warning("No results found.")
            else:
                st.error("Failed to fetch data.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a search query.")
