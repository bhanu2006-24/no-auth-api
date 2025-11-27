import streamlit as st

st.set_page_config(page_title="HTTP Dog", page_icon="🐶")

st.markdown("# 🐶 HTTP Dog")
st.sidebar.header("HTTP Dog")
st.write("Visualizing HTTP Status Codes with Dogs.")

code = st.number_input("Enter HTTP Status Code", min_value=100, max_value=599, value=404)

if code:
    url = f"https://http.dog/{code}.jpg"
    st.image(url, caption=f"Status Code: {code}")
