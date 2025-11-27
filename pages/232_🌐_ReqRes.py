import streamlit as st
import requests

st.set_page_config(page_title="ReqRes", page_icon="🧪")

st.markdown("# 🧪 ReqRes")
st.write("Test your front-end against a real API.")

if st.button("List Users"):
    try:
        response = requests.get("https://reqres.in/api/users?page=1")
        if response.status_code == 200:
            data = response.json()
            for user in data['data']:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(user['avatar'])
                with col2:
                    st.subheader(f"{user['first_name']} {user['last_name']}")
                    st.write(user['email'])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
