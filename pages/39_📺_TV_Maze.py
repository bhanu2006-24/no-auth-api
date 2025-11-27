import streamlit as st
import requests

st.set_page_config(page_title="TV Maze", page_icon="📺")

st.markdown("# 📺 TV Maze")
st.sidebar.header("TV Maze")
st.write(
    """This page searches for TV shows using the [TV Maze API](https://www.tvmaze.com/api)."""
)

query = st.text_input("Enter TV Show Name", "Breaking Bad")

if st.button("Search Shows"):
    if query:
        try:
            response = requests.get(f"https://api.tvmaze.com/search/shows?q={query}")
            if response.status_code == 200:
                data = response.json()
                if data:
                    st.success(f"Found {len(data)} shows:")
                    for item in data:
                        show = item["show"]
                        col1, col2 = st.columns([1, 3])
                        with col1:
                            if show["image"]:
                                st.image(show["image"]["medium"])
                        with col2:
                            st.subheader(show["name"])
                            st.write(f"**Genres:** {', '.join(show['genres'])}")
                            st.write(f"**Rating:** {show['rating']['average']}")
                            st.write(f"**Status:** {show['status']}")
                            if show["summary"]:
                                st.markdown(show["summary"], unsafe_allow_html=True)
                        st.markdown("---")
                else:
                    st.warning("No shows found.")
            else:
                st.error("Failed to fetch shows. The API might be down.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a show name.")
