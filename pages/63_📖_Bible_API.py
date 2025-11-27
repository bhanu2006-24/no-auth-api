import streamlit as st
import requests

st.set_page_config(page_title="Bible Verses", page_icon="📖")

st.title("📖 Bible API")
st.markdown("Get Bible verses using [bible-api.com](https://bible-api.com/).")

reference = st.text_input("Enter Reference (e.g., John 3:16)", "John 3:16")

if st.button("Get Verse"):
    if reference:
        try:
            response = requests.get(f"https://bible-api.com/{reference}")
            if response.status_code == 200:
                data = response.json()
                st.subheader(data['reference'])
                st.markdown(f"_{data['text']}_")
                st.caption(f"Translation: {data['translation_name']}")
            else:
                st.error("Verse not found or invalid reference.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a reference.")
