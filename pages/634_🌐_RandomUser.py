import streamlit as st
import requests

st.set_page_config(page_title="Random User", page_icon="👤")
st.markdown("# 👤 Random User")

if st.button("Generate User"):
    try:
        response = requests.get("https://randomuser.me/api/")
        if response.status_code == 200:
            user = response.json()['results'][0]
            st.image(user['picture']['large'])
            st.header(f"{user['name']['first']} {user['name']['last']}")
            st.write(f"**Email:** {user['email']}")
            st.write(f"**Location:** {user['location']['city']}, {user['location']['country']}")
    except Exception as e:
        st.error(f"Error: {e}")
