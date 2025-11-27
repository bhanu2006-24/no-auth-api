import streamlit as st
import requests

st.set_page_config(page_title="Evil Insult Generator", page_icon="😈")

st.title("😈 Evil Insult Generator")
st.markdown("Generate mean insults using [Evil Insult Generator](https://evilinsult.com/).")

if st.button("Get Insult"):
    try:
        response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
        if response.status_code == 200:
            data = response.json()
            st.header(f"\"{data['insult']}\"")
        else:
            st.error("Failed to generate insult.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
