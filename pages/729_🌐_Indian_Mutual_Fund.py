import streamlit as st
import requests

st.set_page_config(page_title="Indian Mutual Funds", page_icon="💰")
st.markdown("# 💰 Indian Mutual Funds")

if st.button("List Funds (Sample)"):
    try:
        response = requests.get("https://api.mfapi.in/mf")
        if response.status_code == 200:
            data = response.json()
            st.write(f"Total Funds: {len(data)}")
            for fund in data[:10]:
                st.write(f"**{fund['schemeName']}** (Code: {fund['schemeCode']})")
    except Exception as e:
        st.error(f"Error: {e}")
