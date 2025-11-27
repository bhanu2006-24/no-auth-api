import streamlit as st
import requests

st.set_page_config(page_title="Helium", page_icon="🎈")

st.markdown("# 🎈 Helium Network Stats")
st.write("Stats from the Helium blockchain.")

if st.button("Get Stats"):
    try:
        response = requests.get("https://api.helium.io/v1/stats")
        if response.status_code == 200:
            data = response.json()["data"]
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Hotspots", data["counts"]["hotspots"])
                st.metric("Total Blocks", data["counts"]["blocks"])
            with col2:
                st.metric("Challenges", data["counts"]["challenges"])
                st.metric("Consensus Groups", data["counts"]["consensus_groups"])
                
            st.json(data)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
