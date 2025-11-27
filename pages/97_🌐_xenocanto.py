import streamlit as st
import requests

st.set_page_config(page_title="Xeno-canto", page_icon="🐦")

st.markdown("# 🐦 Xeno-canto Bird Sounds")
st.write("Search for bird recordings from around the world.")

query = st.text_input("Search (e.g., 'cnt:brazil' or 'bearded bellbird')", "cnt:brazil")

if st.button("Search Recordings"):
    try:
        with st.spinner("Searching..."):
            response = requests.get(f"https://www.xeno-canto.org/api/2/recordings?query={query}")
            if response.status_code == 200:
                data = response.json()
                recordings = data.get("recordings", [])
                st.write(f"Found {len(recordings)} recordings.")
                
                for rec in recordings[:10]: # Limit to 10
                    st.markdown(f"### {rec['en']} ({rec['gen']} {rec['sp']})")
                    st.write(f"**Location:** {rec['cnt']}, {rec['loc']}")
                    st.audio(rec['file'])
                    st.markdown("---")
            else:
                st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
