import streamlit as st
import requests

st.set_page_config(page_title="Solana RPC", page_icon="⛓️")
st.markdown("# ⛓️ Solana JSON RPC")

if st.button("Get Cluster Version"):
    try:
        payload = {
            "jsonrpc": "2.0", "id": 1,
            "method": "getVersion"
        }
        response = requests.post("https://api.mainnet-beta.solana.com", json=payload)
        if response.status_code == 200:
            st.json(response.json())
    except Exception as e:
        st.error(f"Error: {e}")
