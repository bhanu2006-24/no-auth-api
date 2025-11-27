import streamlit as st
import requests

st.set_page_config(page_title="Jikan Anime Search", page_icon="🕵️")

st.title("🕵️ Jikan Anime Search")
st.markdown("Search for anime using the [Jikan API](https://jikan.moe/) (Unofficial MyAnimeList API).")

search_query = st.text_input("Enter Anime Name", "One Piece")

if st.button("Search"):
    if search_query:
        try:
            response = requests.get(f"https://api.jikan.moe/v4/anime?q={search_query}&limit=5")
            if response.status_code == 200:
                data = response.json()
                results = data['data']
                
                if results:
                    for anime in results:
                        with st.expander(anime['title']):
                            col1, col2 = st.columns([1, 2])
                            with col1:
                                st.image(anime['images']['jpg']['image_url'], use_column_width=True)
                            with col2:
                                st.write(f"**Score:** {anime.get('score', 'N/A')}")
                                st.write(f"**Episodes:** {anime.get('episodes', 'N/A')}")
                                st.write(f"**Status:** {anime.get('status', 'N/A')}")
                                st.write(f"**Synopsis:** {anime.get('synopsis', 'No synopsis available.')}")
                                st.markdown(f"[More Info]({anime['url']})")
                else:
                    st.warning("No results found.")
            else:
                st.error("Error fetching data from Jikan API.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a search query.")
