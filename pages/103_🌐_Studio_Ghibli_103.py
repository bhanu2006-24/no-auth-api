import streamlit as st
import requests

st.set_page_config(page_title="Studio Ghibli", page_icon="🎬")

st.markdown("# 🎬 Studio Ghibli Films")
st.sidebar.header("Studio Ghibli")
st.write("Explore the films of Studio Ghibli.")

if st.button("Load Films"):
    try:
        response = requests.get("https://ghibliapi.vercel.app/films")
        if response.status_code == 200:
            films = response.json()
            for film in films:
                with st.expander(f"{film['title']} ({film['release_date']})"):
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        st.image(film['image'], use_column_width=True)
                    with col2:
                        st.write(f"**Original Title:** {film['original_title']}")
                        st.write(f"**Director:** {film['director']}")
                        st.write(f"**Producer:** {film['producer']}")
                        st.write(f"**Running Time:** {film['running_time']} min")
                        st.write(f"**Rotten Tomatoes:** {film['rt_score']}%")
                        st.write(f"**Description:** {film['description']}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
