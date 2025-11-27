import streamlit as st
import requests

st.set_page_config(page_title="Trace.moe", page_icon="🔍")

st.markdown("# 🔍 Trace.moe")
st.write("Search for anime by screenshot.")

image_url = st.text_input("Enter Image URL", "https://images.plurk.com/32B15UXxymfSMwKGTObY5e.jpg")

if st.button("Trace Anime"):
    try:
        with st.spinner("Tracing..."):
            response = requests.get(f"https://api.trace.moe/search?url={image_url}")
            if response.status_code == 200:
                data = response.json()
                if data["result"]:
                    top_match = data["result"][0]
                    st.success(f"Found: {top_match['filename']}")
                    st.write(f"**Episode:** {top_match['episode']}")
                    st.write(f"**Similarity:** {top_match['similarity']:.2%}")
                    st.video(top_match['video'])
                    st.image(top_match['image'], caption="Scene Snapshot")
                else:
                    st.warning("No match found.")
            else:
                st.error(f"API Error: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {e}")
