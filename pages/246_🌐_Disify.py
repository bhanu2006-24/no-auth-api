import streamlit as st
import requests

st.set_page_config(page_title="Disify", page_icon="📧")

st.markdown("# 📧 Disify")
st.write("Disposable email detector.")

email = st.text_input("Email", "test@tempmail.com")

if st.button("Check"):
    try:
        response = requests.get(f"https://disify.com/api/email/{email}")
        if response.status_code == 200:
            data = response.json()
            st.write(f"**Format:** {data['format']}")
            st.write(f"**Disposable:** {data['disposable']}")
            st.write(f"**DNS:** {data['dns']}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
