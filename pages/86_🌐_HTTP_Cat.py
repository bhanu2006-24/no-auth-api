import streamlit as st

st.set_page_config(page_title="HTTP Cat", page_icon="🐱")

st.markdown("# 🐱 HTTP Cat")
st.sidebar.header("HTTP Cat")
st.write("Visualizing HTTP Status Codes with Cats.")

code = st.number_input("Enter HTTP Status Code", min_value=100, max_value=599, value=200)

if code:
    url = f"https://http.cat/{code}"
    st.image(url, caption=f"Status Code: {code}")
