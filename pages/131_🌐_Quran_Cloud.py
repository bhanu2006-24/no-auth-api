import streamlit as st
import requests

st.set_page_config(page_title="Quran Cloud", page_icon="☁️")

st.markdown("# ☁️ Quran Cloud Audio")
st.write("Listen to the Quran.")

surah = st.number_input("Surah Number", 1, 114, 1)

if st.button("Get Audio"):
    try:
        response = requests.get(f"http://api.alquran.cloud/v1/surah/{surah}/ar.alafasy")
        if response.status_code == 200:
            data = response.json()
            st.subheader(data["data"]["englishName"])
            for ayah in data["data"]["ayahs"][:5]: # Limit to first 5 for demo
                st.write(f"Ayah {ayah['numberInSurah']}")
                st.audio(ayah["audio"])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
