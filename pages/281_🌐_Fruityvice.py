import streamlit as st
import requests

st.set_page_config(page_title="Fruityvice", page_icon="🍎")

st.markdown("# 🍎 Fruityvice")
st.write("Fruit nutrition data.")

fruit = st.text_input("Fruit Name", "apple")

if st.button("Get Info"):
    try:
        response = requests.get(f"https://www.fruityvice.com/api/fruit/{fruit}")
        if response.status_code == 200:
            data = response.json()
            st.subheader(data['name'])
            st.json(data['nutritions'])
        else:
            st.error("Fruit not found.")
    except Exception as e:
        st.error(f"Error: {e}")
