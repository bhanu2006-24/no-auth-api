import streamlit as st

st.set_page_config(page_title="QuickChart QR", page_icon="📱")

st.markdown("# 📱 QuickChart QR")

text = st.text_input("Text/URL", "https://google.com")

if st.button("Generate"):
    url = f"https://quickchart.io/qr?text={text}&size=200"
    st.image(url, caption="QR Code")
