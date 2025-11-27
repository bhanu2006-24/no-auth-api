import streamlit as st
import requests

st.set_page_config(page_title="Disney API", page_icon="🏰")
st.markdown("# 🏰 Disney Characters")

if st.button("Get Character"):
    try:
        response = requests.get("https://api.disneyapi.dev/character?pageSize=1") # Randomize page for better effect ideally
        if response.status_code == 200:
            data = response.json()
            char = data['data'][0] # Just taking the first one
            st.header(char['name'])
            if 'imageUrl' in char:
                st.image(char['imageUrl'])
            st.write(f"**Films:** {', '.join(char['films'])}")
    except Exception as e:
        st.error(f"Error: {e}")
