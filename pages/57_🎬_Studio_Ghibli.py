import streamlit as st
import requests

st.set_page_config(page_title="Studio Ghibli Films", page_icon="🎬")

st.title("🎬 Studio Ghibli Films")
st.markdown("Explore films from Studio Ghibli using the [Studio Ghibli API](https://ghibliapi.herokuapp.com/).")

try:
    response = requests.get("https://ghibliapi.herokuapp.com/films")
    if response.status_code == 200:
        films = response.json()
        
        film_titles = [film['title'] for film in films]
        selected_film_title = st.selectbox("Select a Film", film_titles)
        
        selected_film = next((film for film in films if film['title'] == selected_film_title), None)
        
        if selected_film:
            st.subheader(f"{selected_film['title']} ({selected_film['original_title']})")
            st.image(selected_film['movie_banner'], use_column_width=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Director:** {selected_film['director']}")
                st.write(f"**Producer:** {selected_film['producer']}")
            with col2:
                st.write(f"**Release Date:** {selected_film['release_date']}")
                st.write(f"**Running Time:** {selected_film['running_time']} mins")
            
            st.write(f"**Rotten Tomatoes Score:** {selected_film['rt_score']}")
            st.write(f"**Description:** {selected_film['description']}")
            
    else:
        st.error("Failed to fetch films list.")
except Exception as e:
    st.error(f"An error occurred: {e}")
