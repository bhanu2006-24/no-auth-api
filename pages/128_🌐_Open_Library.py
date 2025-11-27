import streamlit as st
import requests

st.set_page_config(page_title="Open Library", page_icon="🏛️")

st.markdown("# 🏛️ Open Library Search")
st.write("Search for books in the Open Library.")

query = st.text_input("Book Title", "The Lord of the Rings")

if st.button("Search"):
    try:
        response = requests.get(f"https://openlibrary.org/search.json?q={query}&limit=5")
        if response.status_code == 200:
            data = response.json()
            docs = data.get("docs", [])
            for doc in docs:
                st.subheader(doc.get("title"))
                st.write(f"**Author:** {', '.join(doc.get('author_name', []))}")
                st.write(f"**First Published:** {doc.get('first_publish_year')}")
                if "cover_i" in doc:
                    st.image(f"https://covers.openlibrary.org/b/id/{doc['cover_i']}-M.jpg")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
