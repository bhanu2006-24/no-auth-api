import streamlit as st
import requests

st.set_page_config(page_title="More Dog Facts", page_icon="🐕")

st.markdown("# 🐕 More Dog Facts")
st.sidebar.header("More Dog Facts")
st.write("Another source for dog wisdom.")

if st.button("🐕 Fetch Fact"):
    try:
        # Using the same API but styling differently as it was a duplicate in the list
        response = requests.get("http://dog-api.kinduff.com/api/facts")
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                fact = data["facts"][0]
                st.markdown(f"> *{fact}*")
            else:
                st.warning("No facts available.")
        else:
            st.error("API Error.")
    except Exception as e:
        st.error(f"Error: {e}")
