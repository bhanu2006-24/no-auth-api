import streamlit as st
import requests

st.set_page_config(page_title="Website Carbon", page_icon="🌿")

st.markdown("# 🌿 Website Carbon")
st.write("Calculate website carbon footprint.")

url = st.text_input("URL", "https://google.com")

if st.button("Calculate"):
    try:
        response = requests.get(f"https://api.websitecarbon.com/site?url={url}")
        if response.status_code == 200:
            data = response.json()
            st.metric("Green?", str(data['green']))
            st.metric("CO2 per Visit", f"{data['statistics']['co2']['grid']['grams']:.4f} g")
        else:
            st.error("API Error (Site might not be reachable)")
    except Exception as e:
        st.error(f"Error: {e}")
