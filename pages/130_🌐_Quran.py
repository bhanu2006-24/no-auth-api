import streamlit as st
import requests

st.set_page_config(page_title="Quran", page_icon="☪️")

st.markdown("# ☪️ Al-Quran")
st.write("Read verses from the Quran.")

surah = st.number_input("Surah Number", 1, 114, 1)
ayah = st.number_input("Ayah Number", 1, 286, 1)

if st.button("Get Ayah"):
    try:
        response = requests.get(f"http://api.alquran.cloud/v1/ayah/{surah}:{ayah}/en.asad")
        if response.status_code == 200:
            data = response.json()
            st.markdown(f"### {data['data']['text']}")
            st.caption(f"Surah {data['data']['surah']['englishName']}, Ayah {data['data']['numberInSurah']}")
        else:
            st.error("Ayah not found.")
    except Exception as e:
        st.error(f"Error: {e}")
