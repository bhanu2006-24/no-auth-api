import streamlit as st

st.set_page_config(page_title="QR Code", page_icon="📱")

st.markdown("# 📱 QR Code Generator")

text = st.text_input("Text/URL", "https://streamlit.io")
size = st.slider("Size", 100, 500, 200)

if st.button("Generate"):
    url = f"https://api.qrserver.com/v1/create-qr-code/?size={size}x{size}&data={text}"
    st.image(url, caption="QR Code")
