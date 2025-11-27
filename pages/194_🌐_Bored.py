import streamlit as st
import requests

st.set_page_config(page_title="Bored API", page_icon="🥱")

st.markdown("# 🥱 Bored API")
st.write("Let's find you something to do.")

if st.button("I'm Bored"):
    try:
        response = requests.get("https://www.boredapi.com/api/activity")
        if response.status_code == 200:
            data = response.json()
            st.header(data['activity'])
            st.write(f"**Type:** {data['type']}")
            st.write(f"**Participants:** {data['participants']}")
            st.write(f"**Price:** {data['price']}")
        else:
            st.error("API Error (Bored API might be down, it happens often).")
    except Exception as e:
        st.error(f"Error: {e}")
