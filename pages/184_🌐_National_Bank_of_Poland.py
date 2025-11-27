import streamlit as st
import requests

st.set_page_config(page_title="NBP", page_icon="🇵🇱")

st.markdown("# 🇵🇱 National Bank of Poland")

if st.button("Get Rates"):
    try:
        response = requests.get("http://api.nbp.pl/api/exchangerates/tables/A/?format=json")
        if response.status_code == 200:
            data = response.json()[0]
            st.write(f"**Table:** {data['no']}")
            st.write(f"**Date:** {data['effectiveDate']}")
            
            rates = data['rates']
            for rate in rates[:5]:
                st.write(f"**{rate['currency']} ({rate['code']}):** {rate['mid']} PLN")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
