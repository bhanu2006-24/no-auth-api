import streamlit as st
import requests

st.set_page_config(page_title="Crossref", page_icon="📚")

st.markdown("# 📚 Crossref Metadata Search")
st.write("Search for academic works.")

query = st.text_input("Search Query", "machine learning")

if st.button("Search"):
    try:
        response = requests.get(f"https://api.crossref.org/works?query={query}&rows=5")
        if response.status_code == 200:
            data = response.json()
            items = data["message"]["items"]
            for item in items:
                title = item.get("title", ["Untitled"])[0]
                st.subheader(title)
                st.write(f"**DOI:** {item.get('DOI')}")
                st.write(f"**Publisher:** {item.get('publisher')}")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
