import streamlit as st
import requests

st.set_page_config(page_title="Dictionary", page_icon="📖")

st.markdown("# 📖 Dictionary")
st.sidebar.header("Dictionary")
st.write(
    """This page looks up word definitions using the [Free Dictionary API](https://dictionaryapi.dev/)."""
)

word = st.text_input("Enter a word", "hello")

if st.button("Define"):
    if word:
        try:
            response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
            if response.status_code == 200:
                data = response.json()[0]
                st.subheader(data["word"])
                if "phonetic" in data:
                    st.write(f"**Phonetic:** {data['phonetic']}")
                
                for meaning in data["meanings"]:
                    st.markdown(f"### {meaning['partOfSpeech']}")
                    for defn in meaning["definitions"]:
                        st.write(f"- {defn['definition']}")
                        if "example" in defn:
                            st.caption(f"Example: {defn['example']}")
            else:
                st.error("Word not found.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a word.")
