import streamlit as st
import requests

st.set_page_config(page_title="Nationality Predictor", page_icon="👤")

st.markdown("# 👤 Nationality Predictor")
st.sidebar.header("Nationality Predictor")
st.write(
    """This page predicts the nationality of a name using the [Nationalize.io API](https://nationalize.io/)."""
)

name = st.text_input("Enter a name", "Michael")

if st.button("Predict Nationality"):
    if name:
        try:
            response = requests.get(f"https://api.nationalize.io/?name={name}")
            if response.status_code == 200:
                data = response.json()
                if data["country"]:
                    st.success(f"Predictions for {name}:")
                    for country in data["country"]:
                        country_id = country["country_id"]
                        probability = country["probability"]
                        st.write(f"- **{country_id}**: {probability:.2%}")
                else:
                    st.warning("No nationality data found for this name.")
            else:
                st.error("Failed to fetch data. The API might be down.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a name.")
