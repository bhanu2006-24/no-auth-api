import streamlit as st
import requests

st.set_page_config(page_title="DigitalOcean Status", page_icon="🌊")

st.markdown("# 🌊 DigitalOcean Status")
st.write("Real-time status of DigitalOcean services.")

if st.button("Get Status"):
    try:
        response = requests.get("https://status.digitalocean.com/api/v2/summary.json")
        if response.status_code == 200:
            data = response.json()
            st.subheader(data['page']['name'])
            st.write(f"**URL:** {data['page']['url']}")
            st.write(f"**Updated:** {data['page']['updated_at']}")
            
            st.subheader("Components")
            for component in data['components'][:5]: # Show first 5
                status_color = "green" if component['status'] == "operational" else "red"
                st.markdown(f":{status_color}[{component['name']}: {component['status']}]")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
