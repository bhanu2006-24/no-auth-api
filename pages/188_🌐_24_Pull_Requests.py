import streamlit as st
import requests

st.set_page_config(page_title="24 Pull Requests", page_icon="🎄")

st.markdown("# 🎄 24 Pull Requests")
st.write("Giving back to open source for the holidays.")

if st.button("Get Projects"):
    try:
        response = requests.get("https://24pullrequests.com/projects.json")
        if response.status_code == 200:
            data = response.json()
            for project in data[:5]:
                st.subheader(project['name'])
                st.write(project['description'])
                st.markdown(f"[View on GitHub]({project['github_url']})")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
