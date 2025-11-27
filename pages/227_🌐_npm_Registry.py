import streamlit as st
import requests

st.set_page_config(page_title="NPM Registry", page_icon="📦")

st.markdown("# 📦 NPM Registry")
st.write("Search NPM packages.")

query = st.text_input("Search", "react")

if st.button("Search"):
    try:
        response = requests.get(f"https://registry.npmjs.org/-/v1/search?text={query}&size=5")
        if response.status_code == 200:
            data = response.json()
            for obj in data['objects']:
                pkg = obj['package']
                st.subheader(pkg['name'])
                st.write(pkg.get('description', ''))
                st.write(f"v{pkg['version']}")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
