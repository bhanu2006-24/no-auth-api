import streamlit as st
import requests

st.set_page_config(page_title="GrünstromIndex", page_icon="🇩🇪")

st.markdown("# 🇩🇪 GrünstromIndex")
st.write("Green power index for Germany.")

zipcode = st.text_input("Zipcode", "10115")

if st.button("Check"):
    try:
        response = requests.get(f"https://api.corrently.io/v2.0/gsi/prediction?zip={zipcode}")
        if response.status_code == 200:
            data = response.json()
            if data['forecast']:
                current = data['forecast'][0]
                st.metric("GSI Score", current['gsi'])
                st.caption(f"Time: {current['timeStamp']}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
