import streamlit as st
import requests

st.set_page_config(page_title="City Bikes", page_icon="🚲")
st.markdown("# 🚲 City Bikes")

if st.button("Get Networks"):
    try:
        response = requests.get("http://api.citybik.es/v2/networks")
        if response.status_code == 200:
            data = response.json()
            networks = data['networks']
            st.write(f"Total Networks: {len(networks)}")
            for net in networks[:5]:
                st.subheader(net['name'])
                st.write(f"Location: {net['location']['city']}, {net['location']['country']}")
    except Exception as e:
        st.error(f"Error: {e}")
