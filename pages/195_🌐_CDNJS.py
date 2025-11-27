import streamlit as st
import requests

st.set_page_config(page_title="CDNJS", page_icon="⚡")

st.markdown("# ⚡ CDNJS")
st.write("Search for libraries.")

query = st.text_input("Library Name", "react")

if st.button("Search"):
    try:
        response = requests.get(f"https://api.cdnjs.com/libraries?search={query}")
        if response.status_code == 200:
            data = response.json()
            for lib in data['results'][:5]:
                st.subheader(lib['name'])
                st.write(f"**Latest:** {lib['latest']}")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
