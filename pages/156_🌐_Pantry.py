import streamlit as st
import requests
import json

st.set_page_config(page_title="Pantry Cloud", page_icon="🥫")

st.markdown("# 🥫 Pantry Cloud")
st.write("Free JSON storage.")

pantry_id = st.text_input("Pantry ID (Get one at getpantry.cloud)", "")
basket_name = st.text_input("Basket Name", "test_basket")

if st.button("Get Basket"):
    if pantry_id:
        try:
            response = requests.get(f"https://getpantry.cloud/apiv1/pantry/{pantry_id}/basket/{basket_name}")
            if response.status_code == 200:
                st.json(response.json())
            else:
                st.error("Basket not found or Error.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a Pantry ID.")
