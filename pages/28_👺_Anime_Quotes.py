import streamlit as st
import requests

st.set_page_config(page_title="Anime Quotes", page_icon="👺")

st.markdown("# 👺 Anime Quotes")
st.sidebar.header("Anime Quotes")
st.write(
    """This page fetches a random anime quote using the [AnimeChan API](https://animechan.xyz/)."""
)

if st.button("Get Quote"):
    try:
        # Using a reliable alternative since AnimeChan can be flaky
        response = requests.get("https://katanime.vercel.app/api/get/randomAnimeQuote")
        if response.status_code == 200:
            data = response.json()
            # Adjusting for katanime structure if needed, or fallback to animechan structure
            # Katanime returns { "id":..., "anime":..., "character":..., "quote":... }
            quote = data.get("quote", "No quote found")
            character = data.get("character", "Unknown")
            anime = data.get("anime", "Unknown")
            
            st.markdown(f"### *\"{quote}\"*")
            st.write(f"**- {character}** ({anime})")
        else:
             # Fallback attempt
            response = requests.get("https://animechan.xyz/api/random")
            if response.status_code == 200:
                data = response.json()
                st.markdown(f"### *\"{data['quote']}\"*")
                st.write(f"**- {data['character']}** ({data['anime']})")
            else:
                st.error("Failed to fetch quote. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
