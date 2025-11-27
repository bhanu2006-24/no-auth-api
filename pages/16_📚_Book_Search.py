import streamlit as st
import requests

st.set_page_config(page_title="Book Search", page_icon="📚")

st.markdown("# 📚 Book Search")
st.sidebar.header("Book Search")
st.write(
    """This page searches for books using the [Open Library API](https://openlibrary.org/)."""
)

query = st.text_input("Enter book title", "The Lord of the Rings")

if st.button("Search Books"):
    if query:
        try:
            response = requests.get(f"https://openlibrary.org/search.json?q={query}")
            if response.status_code == 200:
                data = response.json()
                if data["numFound"] > 0:
                    st.success(f"Found {data['numFound']} books. Showing top 5:")
                    for book in data["docs"][:5]:
                        title = book.get("title", "Unknown Title")
                        author = ", ".join(book.get("author_name", ["Unknown Author"]))
                        year = book.get("first_publish_year", "Unknown Year")
                        st.markdown(f"### {title}")
                        st.write(f"**Author:** {author}")
                        st.write(f"**First Published:** {year}")
                        st.markdown("---")
                else:
                    st.warning("No books found.")
            else:
                st.error("Failed to fetch books. The API might be down.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a book title.")
