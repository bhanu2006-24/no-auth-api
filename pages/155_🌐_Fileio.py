import streamlit as st
import requests

st.set_page_config(page_title="File.io", page_icon="📤")

st.markdown("# 📤 File.io")
st.write("Ephemeral file sharing. Files are deleted after one download.")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    if st.button("Upload"):
        try:
            files = {'file': uploaded_file}
            response = requests.post('https://file.io', files=files)
            if response.status_code == 200:
                data = response.json()
                if data['success']:
                    st.success("File Uploaded!")
                    st.text_input("Download Link", data['link'])
                    st.warning(f"This link will expire in {data['expiry']}.")
                else:
                    st.error("Upload failed.")
            else:
                st.error(f"API Error: {response.status_code}")
        except Exception as e:
            st.error(f"Error: {e}")
