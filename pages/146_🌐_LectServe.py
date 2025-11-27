import streamlit as st
import requests

st.set_page_config(page_title="LectServe", page_icon="📖")

st.markdown("# 📖 LectServe")
st.write("Lectionary for the day.")

if st.button("Get Lectionary"):
    try:
        response = requests.get("http://www.lectserve.com/u/json/today")
        if response.status_code == 200:
            data = response.json()
            st.write(f"**Date:** {data.get('date')}")
            # Note: Response structure varies, printing raw for safety if simple keys missing
            st.json(data)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
