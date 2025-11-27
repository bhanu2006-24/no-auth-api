import streamlit as st
import requests

st.set_page_config(page_title="Bitcoin Price", page_icon="💰")

st.markdown("# 💰 Bitcoin Price")
st.sidebar.header("Bitcoin Price")
st.write(
    """This page fetches the current Bitcoin price from the [CoinDesk API](https://www.coindesk.com/coindesk-api)."""
)

if st.button("Get Price"):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        if response.status_code == 200:
            data = response.json()
            bpi = data["bpi"]
            st.write(f"**Updated:** {data['time']['updated']}")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("USD", f"${bpi['USD']['rate']}")
            with col2:
                st.metric("GBP", f"£{bpi['GBP']['rate']}")
            with col3:
                st.metric("EUR", f"€{bpi['EUR']['rate']}")
                
            st.caption(data["disclaimer"])
        else:
            st.error("Failed to fetch price. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
