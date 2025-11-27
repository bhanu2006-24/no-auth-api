import streamlit as st

st.set_page_config(page_title="AI Person", page_icon="👤")
st.markdown("# 👤 This Person Does Not Exist")

if st.button("Get Image"):
    st.image("https://thispersondoesnotexist.com/", caption="AI Generated Face")
