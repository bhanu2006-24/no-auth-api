import streamlit as st
import requests

st.set_page_config(page_title="Binary Jazz Genre Generator", page_icon="🎷")

st.title("🎷 Binary Jazz Genre Generator")
st.markdown("Generate completely new music genres using [Binary Jazz](https://binaryjazz.us/).")

if st.button("Generate Genre"):
    try:
        response = requests.get("https://binaryjazz.us/wp-json/genrenator/v1/genre/")
        if response.status_code == 200:
            genre = response.json()
            st.header(genre)
            
            # Also get a story if available? The API seems simple.
            # Let's try to get a story too if the endpoint exists, but the main one is just genre.
            # There is a story endpoint: https://binaryjazz.us/wp-json/genrenator/v1/story/
            
            story_response = requests.get("https://binaryjazz.us/wp-json/genrenator/v1/story/")
            if story_response.status_code == 200:
                story = story_response.json()
                st.markdown(f"_{story}_")
                
        else:
            st.error("Failed to generate genre.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
