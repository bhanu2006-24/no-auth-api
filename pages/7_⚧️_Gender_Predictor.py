import streamlit as st
import requests

st.set_page_config(page_title="Gender Predictor", page_icon="⚧️")

st.markdown("# ⚧️ Gender Predictor")
st.sidebar.header("Gender Predictor")
st.write(
    """This page predicts the gender of a person based on their name using the [Genderize API](https://genderize.io/)."""
)

name = st.text_input("Enter a name", "Sarah")

if st.button("Predict Gender"):
    if name:
        try:
            response = requests.get(f"https://api.genderize.io/?name={name}")
            if response.status_code == 200:
                data = response.json()
                if data["gender"]:
                    st.success(f"Predicted gender for {name}: **{data['gender'].capitalize()}**")
                    st.write(f"Probability: {data['probability']:.2%}")
                    st.write(f"(Based on {data['count']} samples)")
                else:
                    st.warning("Could not predict gender for this name.")
            else:
                st.error("Failed to fetch data. The API might be down.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a name.")
