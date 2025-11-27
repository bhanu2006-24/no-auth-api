import streamlit as st
import requests

st.set_page_config(page_title="NASA APOD", page_icon="🚀")
st.markdown("# 🚀 NASA APOD")

if st.button("Get Picture of the Day"):
    try:
        response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
        if response.status_code == 200:
            data = response.json()
            st.header(data['title'])
            if data['media_type'] == 'image':
                st.image(data['url'])
            else:
                st.video(data['url'])
            st.write(data['explanation'])
        else:
            st.error("API Error (Demo key might be rate limited)")
    except Exception as e:
        st.error(f"Error: {e}")
