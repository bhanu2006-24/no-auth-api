import streamlit as st
import requests

st.set_page_config(page_title="PoetryDB", page_icon="📜")

st.title("📜 PoetryDB")
st.markdown("Fetch classic poems using [PoetryDB](https://poetrydb.org/).")

option = st.selectbox("Search by", ["Random Poem", "Author", "Title"])

if option == "Random Poem":
    if st.button("Get Random Poem"):
        try:
            response = requests.get("https://poetrydb.org/random")
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and len(data) > 0:
                    poem = data[0]
                    st.subheader(poem['title'])
                    st.write(f"**By {poem['author']}**")
                    st.text("\n".join(poem['lines']))
                else:
                    st.error("No poem found.")
            else:
                st.error("Failed to fetch poem.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

elif option == "Author":
    author = st.text_input("Enter Author Name", "Emily Dickinson")
    if st.button("Search Author"):
        try:
            response = requests.get(f"https://poetrydb.org/author/{author}")
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    st.success(f"Found {len(data)} poems by {author}")
                    selected_poem_title = st.selectbox("Select a Poem", [p['title'] for p in data])
                    selected_poem = next((p for p in data if p['title'] == selected_poem_title), None)
                    if selected_poem:
                        st.subheader(selected_poem['title'])
                        st.text("\n".join(selected_poem['lines']))
                else:
                    st.warning("No poems found for this author.")
            else:
                st.error("Failed to fetch poems.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

elif option == "Title":
    title = st.text_input("Enter Poem Title", "Ozymandias")
    if st.button("Search Title"):
        try:
            response = requests.get(f"https://poetrydb.org/title/{title}")
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    for poem in data:
                        st.subheader(poem['title'])
                        st.write(f"**By {poem['author']}**")
                        st.text("\n".join(poem['lines']))
                        st.markdown("---")
                else:
                    st.warning("No poems found with this title.")
            else:
                st.error("Failed to fetch poems.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
