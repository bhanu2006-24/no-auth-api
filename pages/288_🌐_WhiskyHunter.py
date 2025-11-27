import streamlit as st
import requests

st.set_page_config(page_title="WhiskyHunter", page_icon="🥃")

st.markdown("# 🥃 WhiskyHunter")

if st.button("Get Auctions"):
    try:
        response = requests.get("https://whiskyhunter.net/api/auctions_data/?format=json")
        if response.status_code == 200:
            data = response.json()
            for auction in data[:5]:
                st.subheader(auction['dt'])
                st.write(f"**Auction:** {auction['auction_name']}")
                st.write(f"**Winning Bid:** {auction['winning_bid_max']}")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
