import streamlit as st
import requests

st.set_page_config(page_title="Wolne Lektury", page_icon="🇵🇱")

st.markdown("# 🇵🇱 Wolne Lektury")
st.write("Free Polish Literature.")

if st.button("Get Random Book"):
    try:
        # Fetching a known book for demo as random endpoint isn't direct
        response = requests.get("https://wolnelektury.pl/api/books/studnia-i-wahadlo/")
        if response.status_code == 200:
            book = response.json()
            st.header(book['title'])
            st.write(f"**Author:** {book['authors'][0]['name']}")
            st.image(book['cover'], use_column_width=True)
            st.markdown(f"[Read Online]({book['url']})")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
