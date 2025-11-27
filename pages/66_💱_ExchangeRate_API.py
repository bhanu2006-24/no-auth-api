import streamlit as st
import requests

st.set_page_config(page_title="Exchange Rates", page_icon="💱")

st.title("💱 Exchange Rates")
st.markdown("Get current exchange rates using [ExchangeRate-API](https://www.exchangerate-api.com/).")

base_currency = st.selectbox("Select Base Currency", ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"])

if st.button("Get Rates"):
    try:
        response = requests.get(f"https://open.er-api.com/v6/latest/{base_currency}")
        if response.status_code == 200:
            data = response.json()
            st.write(f"**Last Update:** {data['time_last_update_utc']}")
            
            rates = data['rates']
            # Display a few key rates
            key_currencies = ["USD", "EUR", "GBP", "JPY", "INR", "AUD", "CAD", "CHF", "CNY"]
            
            col1, col2 = st.columns(2)
            for i, currency in enumerate(key_currencies):
                if currency != base_currency:
                    with (col1 if i % 2 == 0 else col2):
                        st.metric(label=currency, value=rates.get(currency, "N/A"))
            
            with st.expander("View All Rates"):
                st.json(rates)
        else:
            st.error("Failed to fetch exchange rates.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
