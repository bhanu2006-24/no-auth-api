import streamlit as st
import requests

st.set_page_config(page_title="Deck of Cards", page_icon="🃏")
st.markdown("# 🃏 Deck of Cards")

if st.button("Draw a Card"):
    try:
        # Create a new deck first
        deck_response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
        if deck_response.status_code == 200:
            deck_id = deck_response.json()['deck_id']
            # Draw a card
            draw_response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1")
            if draw_response.status_code == 200:
                card = draw_response.json()['cards'][0]
                st.image(card['image'], caption=f"{card['value']} of {card['suit']}")
    except Exception as e:
        st.error(f"Error: {e}")
