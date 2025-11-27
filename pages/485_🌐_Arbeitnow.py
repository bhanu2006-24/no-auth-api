import streamlit as st
import requests

st.set_page_config(page_title="Arbeitnow", page_icon="💼")
st.markdown("# 💼 Arbeitnow")
st.write("Jobs in Europe.")

if st.button("Get Jobs"):
    try:
        response = requests.get("https://www.arbeitnow.com/api/job-board-api")
        if response.status_code == 200:
            data = response.json()
            for job in data['data'][:5]:
                st.subheader(job['title'])
                st.write(f"**Company:** {job['company_name']}")
                st.write(f"**Location:** {job['location']}")
                st.markdown(f"[Apply]({job['url']})")
    except Exception as e:
        st.error(f"Error: {e}")
