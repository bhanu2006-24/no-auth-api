import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="CoinCap Crypto Prices", page_icon="💰")

st.title("💰 CoinCap Crypto Prices")
st.markdown("Get real-time cryptocurrency prices using [CoinCap](https://coincap.io/).")

if st.button("Get Top 10 Cryptos"):
    try:
        response = requests.get("https://api.coincap.io/v2/assets?limit=10")
        if response.status_code == 200:
            data = response.json()['data']
            
            # Create a DataFrame for better display
            df = pd.DataFrame(data)
            df = df[['rank', 'name', 'symbol', 'priceUsd', 'changePercent24Hr']]
            df.columns = ['Rank', 'Name', 'Symbol', 'Price (USD)', '24h Change (%)']
            
            # Format numbers
            df['Price (USD)'] = df['Price (USD)'].astype(float).map('${:,.2f}'.format)
            df['24h Change (%)'] = df['24h Change (%)'].astype(float).map('{:,.2f}%'.format)
            
            st.table(df)
        else:
            st.error("Failed to fetch crypto data.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
