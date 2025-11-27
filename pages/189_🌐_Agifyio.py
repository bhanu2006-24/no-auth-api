import streamlit as st
import requests

st.set_page_config(page_title="Agify.io", page_icon="👴")

st.markdown("# 👴 Agify.io")
st.write("Predict age from name.")

name = st.text_input("Name", "Michael")

if st.button("Predict Age"):
    try:
        response = requests.get(f"https://api.agify.io?name={name}")
        if response.status_code == 200:
            data = response.json()
            st.metric("Predicted Age", data['age'])
            st.caption(f"Count: {data['count']}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
