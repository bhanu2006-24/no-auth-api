import streamlit as st
import requests

st.set_page_config(page_title="CoinDesk", page_icon="📰")

st.markdown("# 📰 CoinDesk BPI")
st.write("Bitcoin Price Index.")

if st.button("Get Price"):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        if response.status_code == 200:
            data = response.json()
            st.subheader(data['chartName'])
            st.caption(f"Updated: {data['time']['updated']}")
            
            cols = st.columns(3)
            for i, (currency, info) in enumerate(data['bpi'].items()):
                with cols[i]:
                    st.metric(currency, f"{info['symbol']}{info['rate']}")
                    st.caption(info['description'])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
