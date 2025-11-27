import streamlit as st
import requests

st.set_page_config(page_title="Biriyani As A Service", page_icon="🍛")

st.title("🍛 Biriyani As A Service")
st.markdown("Get random biriyani images using [Biriyani As A Service](https://biriyani.asad.pro/).")

if st.button("Get Biriyani"):
    try:
        response = requests.get("https://biriyani.asad.pro/api/image")
        if response.status_code == 200:
            data = response.json()
            st.image(data["image"], caption="Biriyani Time!", use_column_width=True)
        else:
            st.error("Failed to fetch biriyani.")
    except Exception as e:
        st.error(f"Error: {e}")
