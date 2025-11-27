import streamlit as st
import requests

st.set_page_config(page_title="0x0.st", page_icon="🚫")

st.markdown("# 🚫 The Null Pointer")
st.write("No-bullshit file hosting.")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    if st.button("Upload"):
        try:
            files = {'file': uploaded_file}
            response = requests.post('https://0x0.st', files=files)
            if response.status_code == 200:
                st.success("Uploaded!")
                st.text_input("URL", response.text.strip())
            else:
                st.error("Upload failed.")
        except Exception as e:
            st.error(f"Error: {e}")
