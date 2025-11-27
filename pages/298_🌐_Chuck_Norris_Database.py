import streamlit as st
import requests

st.set_page_config(page_title="ICNDb", page_icon="👊")

st.markdown("# 👊 ICNDb")
st.write("Internet Chuck Norris Database.")

if st.button("Get Joke"):
    try:
        response = requests.get("http://api.icndb.com/jokes/random")
        if response.status_code == 200:
            data = response.json()
            st.header(data['value']['joke'])
        else:
            st.error("API Error (ICNDb is often down, try Chuck Norris IO page).")
    except Exception as e:
        st.error(f"Error: {e}")
