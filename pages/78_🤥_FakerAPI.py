import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Faker API", page_icon="🤥")

st.title("🤥 Faker API")
st.markdown("Generate fake data for testing using [FakerAPI](https://fakerapi.it/).")

resource = st.selectbox("Select Resource", ["persons", "companies", "addresses", "books", "credit_cards"])
quantity = st.slider("Quantity", 1, 20, 5)

if st.button("Generate Data"):
    try:
        response = requests.get(f"https://fakerapi.it/api/v1/{resource}?_quantity={quantity}")
        if response.status_code == 200:
            data = response.json()
            if data['code'] == 200:
                records = data['data']
                st.success(f"Generated {len(records)} records.")
                st.dataframe(pd.DataFrame(records))
            else:
                st.error("API returned an error.")
        else:
            st.error("Failed to fetch fake data.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
