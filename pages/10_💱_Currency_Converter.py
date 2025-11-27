import streamlit as st
import requests

st.set_page_config(page_title="Currency Converter", page_icon="💱")

st.markdown("# 💱 Currency Converter")
st.sidebar.header("Currency Converter")
st.write(
    """This page converts currencies using the [Frankfurter API](https://www.frankfurter.app/)."""
)

amount = st.number_input("Amount", value=10.0)
from_currency = st.selectbox("From", ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"])
to_currency = st.selectbox("To", ["EUR", "USD", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"])

if st.button("Convert"):
    if from_currency != to_currency:
        try:
            response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
            if response.status_code == 200:
                data = response.json()
                converted_amount = data["rates"][to_currency]
                st.success(f"{amount} {from_currency} = **{converted_amount} {to_currency}**")
                st.caption(f"Date: {data['date']}")
            else:
                st.error("Failed to fetch exchange rates. The API might be down.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please select different currencies.")
