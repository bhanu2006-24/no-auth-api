import streamlit as st
import requests

st.set_page_config(page_title="Bhagavad Gita", page_icon="🕉️")

st.markdown("# 🕉️ Bhagavad Gita")
st.write("Read verses from the Bhagavad Gita.")

if st.button("Get Random Verse"):
    try:
        response = requests.get("https://gita-api.vercel.app/random-verse")
        if response.status_code == 200:
            data = response.json()
            # The API structure might vary, adjusting based on common response
            st.subheader(f"Chapter {data.get('chapter_no')}, Verse {data.get('verse_no')}")
            st.markdown(f"**Sanskrit:** {data.get('slok', '')}")
            st.markdown(f"**Translation:** {data.get('transliteration', '')}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
