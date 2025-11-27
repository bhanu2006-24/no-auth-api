import streamlit as st
import requests

st.set_page_config(page_title="CoinGecko Market", page_icon="🦎")

st.title("🦎 CoinGecko Market Data")
st.markdown("Get cryptocurrency market data using [CoinGecko](https://www.coingecko.com/).")

coin_id = st.text_input("Enter Coin ID (e.g., bitcoin, ethereum)", "bitcoin")

if st.button("Get Coin Data"):
    if coin_id:
        try:
            response = requests.get(f"https://api.coingecko.com/api/v3/coins/{coin_id}")
            if response.status_code == 200:
                data = response.json()
                
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(data['image']['large'], use_column_width=True)
                with col2:
                    st.subheader(f"{data['name']} ({data['symbol'].upper()})")
                    st.write(f"**Current Price:** ${data['market_data']['current_price']['usd']:,}")
                    st.write(f"**Market Cap:** ${data['market_data']['market_cap']['usd']:,}")
                    st.write(f"**24h High:** ${data['market_data']['high_24h']['usd']:,}")
                    st.write(f"**24h Low:** ${data['market_data']['low_24h']['usd']:,}")
                
                st.markdown("### Description")
                # Description can be HTML, so we use unsafe_allow_html=True or just strip tags if needed. 
                # Streamlit markdown handles some HTML but let's be safe.
                st.markdown(data['description']['en'], unsafe_allow_html=True)
                
            else:
                st.error("Coin not found or API limit reached.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a coin ID.")
