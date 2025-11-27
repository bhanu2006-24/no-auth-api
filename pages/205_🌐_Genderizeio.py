import streamlit as st
import requests

st.set_page_config(page_title="Genderize.io", page_icon="⚧️")

st.markdown("# ⚧️ Genderize.io")
st.write("Predict gender from a name.")

name = st.text_input("Name", "Kim")

if st.button("Predict"):
    try:
        response = requests.get(f"https://api.genderize.io?name={name}")
        if response.status_code == 200:
            data = response.json()
            if data['gender']:
                st.metric("Gender", data['gender'].capitalize(), f"Probability: {data['probability']:.0%}")
                st.caption(f"Based on {data['count']} entries")
            else:
                st.warning("Could not predict gender.")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
