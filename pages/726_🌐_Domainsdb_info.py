import streamlit as st
import requests

st.set_page_config(page_title="DomainsDB", page_icon="🌐")
st.markdown("# 🌐 DomainsDB")

query = st.text_input("Search Domains", "facebook")

if st.button("Search"):
    try:
        response = requests.get(f"https://api.domainsdb.info/v1/domains/search?domain={query}")
        if response.status_code == 200:
            data = response.json()
            st.write(f"Found {len(data.get('domains', []))} domains.")
            for d in data.get('domains', [])[:10]:
                st.write(f"**{d['domain']}** (Create Date: {d.get('create_date', 'N/A')})")
    except Exception as e:
        st.error(f"Error: {e}")
