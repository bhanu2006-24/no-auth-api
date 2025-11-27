import streamlit as st

st.set_page_config(page_title="Icons8", page_icon="🎱")

st.markdown("# 🎱 Icons8")
st.write("Search for icons on Icons8.")

query = st.text_input("Search Icons", "home")

if st.button("Search"):
    st.markdown(f"**[Click here to search '{query}' on Icons8](https://icons8.com/icons/set/{query})**")
    st.info("Icons8 does not have a free public API for direct embedding without an API key, but you can browse their massive library via the link above.")
