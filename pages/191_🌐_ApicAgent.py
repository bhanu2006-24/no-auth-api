import streamlit as st

st.set_page_config(page_title="ApicAgent", page_icon="🕵️")

st.markdown("# 🕵️ ApicAgent")
st.write("User Agent parser.")

ua = st.text_input("User Agent String", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)")

if st.button("Parse"):
    st.info("The public endpoint for this API seems to be offline or changed. Please check documentation.")
