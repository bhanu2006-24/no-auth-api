import streamlit as st
import requests

st.set_page_config(page_title="Vadivelu HTTP Codes", page_icon="🎭")

st.title("🎭 Vadivelu HTTP Codes")
st.markdown("Get Vadivelu reactions for HTTP status codes using [Vadivelu JSON](https://vadivelu.asad.pro/).")

code = st.number_input("HTTP Status Code", min_value=100, max_value=599, value=200)

if st.button("Get Reaction"):
    try:
        # The API seems to be https://vadivelu.asad.pro/api/id/:id
        # Or maybe just images?
        # Let's try to find the image URL pattern or fetch JSON
        # Docs: https://vadivelu.asad.pro/
        # It says "GET /api/http/:code"
        
        url = f"https://vadivelu.asad.pro/api/http/{code}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            st.image(data["image"], caption=f"Status {code}", use_column_width=True)
        else:
            st.error("Reaction not found for this code.")
    except Exception as e:
        st.error(f"Error: {e}")
