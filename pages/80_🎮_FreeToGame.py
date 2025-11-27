import streamlit as st
import requests

st.set_page_config(page_title="Free Games", page_icon="🎮")

st.title("🎮 FreeToGame")
st.markdown("Discover free-to-play games using [FreeToGame API](https://www.freetogame.com/).")

category = st.selectbox("Select Category", ["shooter", "mmorpg", "strategy", "moba", "racing", "sports", "social", "sandbox", "open-world", "survival", "pvp", "pve", "pixel", "voxel", "zombie", "turn-based", "first-person", "third-person", "top-down", "tank", "space", "sailing", "side-scroller", "superhero", "permadeath", "card", "battle-royale", "mmo", "mmofps", "mmotps", "3d", "2d", "anime", "fantasy", "sci-fi", "fighting", "action-rpg", "action", "military", "martial-arts", "flight", "low-spec", "tower-defense", "horror", "mmorts"])

if st.button("Find Games"):
    try:
        response = requests.get(f"https://www.freetogame.com/api/games?category={category}")
        if response.status_code == 200:
            games = response.json()
            st.success(f"Found {len(games)} games.")
            
            for game in games[:10]: # Limit to 10 for display
                with st.expander(game['title']):
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        st.image(game['thumbnail'], use_column_width=True)
                    with col2:
                        st.write(f"**Genre:** {game['genre']}")
                        st.write(f"**Platform:** {game['platform']}")
                        st.write(f"**Publisher:** {game['publisher']}")
                        st.write(f"**Description:** {game['short_description']}")
                        st.markdown(f"[Play Now]({game['game_url']})")
        else:
            st.error("Failed to fetch games.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
