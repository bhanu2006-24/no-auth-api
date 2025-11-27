import streamlit as st
import requests

st.set_page_config(page_title="NASA APOD", page_icon="🌌")

st.title("🌌 NASA Astronomy Picture of the Day")
st.markdown("Get the Astronomy Picture of the Day using [NASA API](https://api.nasa.gov/).")

# Note: Using DEMO_KEY which has rate limits.
api_key = "DEMO_KEY"

if st.button("Get Picture"):
    try:
        response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")
        if response.status_code == 200:
            data = response.json()
            st.subheader(data['title'])
            
            if data['media_type'] == 'image':
                st.image(data['url'], caption=data['date'], use_column_width=True)
            elif data['media_type'] == 'video':
                st.video(data['url'])
            
            st.write(data['explanation'])
            if 'copyright' in data:
                st.caption(f"Copyright: {data['copyright']}")
        else:
            st.error("Failed to fetch APOD. Rate limit might be exceeded.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
