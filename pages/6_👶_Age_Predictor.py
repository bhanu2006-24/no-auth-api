import streamlit as st
import requests

st.set_page_config(page_title="Age Predictor", page_icon="👶")

st.markdown("# 👶 Age Predictor")
st.sidebar.header("Age Predictor")
st.write(
    """This page predicts the age of a person based on their name using the [Agify API](https://agify.io/)."""
)

name = st.text_input("Enter a name", "Michael")

if st.button("Predict Age"):
    if name:
        try:
            response = requests.get(f"https://api.agify.io/?name={name}")
            if response.status_code == 200:
                data = response.json()
                if data["age"] is not None:
                    st.success(f"Predicted age for {name}: **{data['age']}** years old")
                    st.write(f"(Based on {data['count']} samples)")
                else:
                    st.warning("Could not predict age for this name.")
            else:
                st.error("Failed to fetch data. The API might be down.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a name.")
