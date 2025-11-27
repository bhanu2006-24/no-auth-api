import streamlit as st
import requests

st.set_page_config(page_title="Dog Facts", page_icon="🐶")

st.markdown("# 🐶 Dog Facts")
st.sidebar.header("Dog Facts")
st.write("Learn something new about dogs!")

if st.button("🐶 Tell me about dogs"):
    try:
        response = requests.get("http://dog-api.kinduff.com/api/facts")
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                fact = data["facts"][0]
                st.success(f"**Woof!** {fact}")
            else:
                st.warning("No facts available right now.")
        else:
            st.error("API Error.")
    except Exception as e:
        st.error(f"Error: {e}")
