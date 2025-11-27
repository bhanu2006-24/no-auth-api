import streamlit as st
import requests

st.set_page_config(page_title="Frankfurter", page_icon="🌭")

st.markdown("# 🌭 Frankfurter")
st.write("ECB exchange rates.")

amount = st.number_input("Amount (EUR)", 1, 10000, 1)
to_currency = st.selectbox("To Currency", ["USD", "GBP", "JPY", "CHF", "CAD", "AUD"])

if st.button("Convert"):
    try:
        response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from=EUR&to={to_currency}")
        if response.status_code == 200:
            data = response.json()
            st.success(f"{amount} EUR = {data['rates'][to_currency]} {to_currency}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
