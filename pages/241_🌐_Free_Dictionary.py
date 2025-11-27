import streamlit as st
import requests

st.set_page_config(page_title="Free Dictionary", page_icon="📖")

st.markdown("# 📖 Free Dictionary")

word = st.text_input("Word", "hello")

if st.button("Define"):
    try:
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if response.status_code == 200:
            data = response.json()[0]
            st.subheader(data['word'])
            if 'phonetics' in data and data['phonetics']:
                st.write(f"/{data['phonetics'][0].get('text', '')}/")
            
            for meaning in data['meanings']:
                st.write(f"**{meaning['partOfSpeech']}**")
                for defn in meaning['definitions'][:2]:
                    st.write(f"- {defn['definition']}")
        else:
            st.error("Word not found.")
    except Exception as e:
        st.error(f"Error: {e}")
