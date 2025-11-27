import streamlit as st
import requests
import json

st.set_page_config(page_title="Steem", page_icon="🪙")

st.markdown("# 🪙 Steem Blockchain")
st.write("Get global properties of the Steem blockchain.")

if st.button("Get Properties"):
    try:
        payload = {
            "jsonrpc": "2.0",
            "method": "condenser_api.get_dynamic_global_properties",
            "params": [],
            "id": 1
        }
        response = requests.post("https://api.steemit.com", json=payload)
        if response.status_code == 200:
            data = response.json().get("result", {})
            st.metric("Head Block Number", data.get("head_block_number"))
            st.metric("Total Vesting Fund Steem", data.get("total_vesting_fund_steem"))
            st.metric("Time", data.get("time"))
            st.json(data)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
