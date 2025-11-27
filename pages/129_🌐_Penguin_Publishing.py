import streamlit as st
import requests
import xml.etree.ElementTree as ET

st.set_page_config(page_title="Penguin Publishing", page_icon="🐧")

st.markdown("# 🐧 Penguin Publishing")
st.write("Search for books published by Penguin.")

query = st.text_input("Author Name", "Grisham")

if st.button("Search"):
    try:
        response = requests.get(f"https://reststop.randomhouse.com/resources/works/?start=0&max=5&expandLevel=1&search={query}", headers={"Accept": "application/json"})
        if response.status_code == 200:
            # The API might return JSON if requested, otherwise XML
            try:
                data = response.json()
                works = data.get("work", [])
                if isinstance(works, dict): works = [works] # Handle single result
                
                for work in works:
                    st.subheader(work.get("titleweb"))
                    st.write(f"**Author:** {work.get('authorweb')}")
                    st.markdown("---")
            except:
                st.warning("Could not parse response (likely XML).")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
