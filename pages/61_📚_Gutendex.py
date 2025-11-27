import streamlit as st
import requests

st.set_page_config(page_title="Gutendex Books", page_icon="📚")

st.title("📚 Gutendex (Project Gutenberg Books)")
st.markdown("Search for free ebooks using [Gutendex](https://gutendex.com/).")

search_query = st.text_input("Search for books (title, author, etc.)", "Frankenstein")

if st.button("Search"):
    if search_query:
        try:
            response = requests.get(f"https://gutendex.com/books?search={search_query}")
            if response.status_code == 200:
                data = response.json()
                books = data['results']
                
                if books:
                    for book in books:
                        with st.expander(book['title']):
                            col1, col2 = st.columns([1, 3])
                            with col1:
                                if book['formats'].get('image/jpeg'):
                                    st.image(book['formats']['image/jpeg'], use_column_width=True)
                            with col2:
                                authors = ", ".join([author['name'] for author in book['authors']])
                                st.write(f"**Author(s):** {authors}")
                                st.write(f"**Languages:** {', '.join(book['languages'])}")
                                st.write(f"**Downloads:** {book['download_count']}")
                                
                                # Links to read
                                if book['formats'].get('text/html'):
                                    st.markdown(f"[Read Online (HTML)]({book['formats']['text/html']})")
                                if book['formats'].get('application/epub+zip'):
                                    st.markdown(f"[Download EPUB]({book['formats']['application/epub+zip']})")
                else:
                    st.warning("No books found.")
            else:
                st.error("Failed to fetch books.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a search term.")
