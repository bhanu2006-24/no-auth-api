import streamlit as st
import requests

st.set_page_config(page_title="Anime Facts", page_icon="🎌")

st.title("🎌 Anime Facts")
st.markdown("Get random facts about various anime using the [Anime Facts API](https://chandan-02.github.io/anime-facts-rest-api/).")

# First, fetch the list of available anime
try:
    response = requests.get("https://anime-facts-rest-api.herokuapp.com/api/v1")
    # Note: The URL in the list was github.io but the actual API is often on heroku or similar.
    # Let's try the common one. If it fails, we might need to fallback or check the github io page for the real endpoint.
    # The github io page says: Base URL: https://anime-facts-rest-api.herokuapp.com/api/v1
    
    if response.status_code == 200:
        data = response.json()
        if data['success']:
            anime_list = data['data']
            anime_names = [anime['anime_name'] for anime in anime_list]
            
            selected_anime = st.selectbox("Select an Anime", anime_names)
            
            if st.button("Get Fact"):
                # Fetch fact for selected anime
                # The anime name in the selectbox needs to be formatted for the URL (usually replacing spaces with underscores or just using the 'anime_id' or 'anime_name' from the object if it's clean)
                # The API returns 'anime_name' like "bleach", "black_clover". It seems they are already slugified.
                
                fact_response = requests.get(f"https://anime-facts-rest-api.herokuapp.com/api/v1/{selected_anime}")
                if fact_response.status_code == 200:
                    fact_data = fact_response.json()
                    if fact_data['success']:
                        facts = fact_data['data']
                        import random
                        random_fact = random.choice(facts)
                        st.info(random_fact['fact'])
                        st.image(fact_data['img'], caption=selected_anime, width=300)
                    else:
                        st.error("No facts found.")
                else:
                    st.error("Failed to fetch facts.")
        else:
            st.error("API returned unsuccessful response.")
    else:
        # Fallback if the main list endpoint fails or is different
        st.warning("Could not fetch anime list. Trying a default.")
        if st.button("Get Random Naruto Fact"):
             r = requests.get("https://anime-facts-rest-api.herokuapp.com/api/v1/naruto")
             if r.status_code == 200:
                 d = r.json()
                 import random
                 st.info(random.choice(d['data'])['fact'])
except Exception as e:
    st.error(f"An error occurred: {e}")
