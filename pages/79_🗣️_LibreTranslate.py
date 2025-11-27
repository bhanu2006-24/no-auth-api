import streamlit as st
import requests

st.set_page_config(page_title="LibreTranslate", page_icon="🗣️")

st.title("🗣️ LibreTranslate")
st.markdown("Translate text using [LibreTranslate](https://libretranslate.com/).")
st.info("Note: Using the public instance which may have rate limits.")

text_to_translate = st.text_area("Enter text to translate", "Hello, how are you?")
target_lang = st.selectbox("Target Language", ["es", "fr", "de", "it", "pt", "ru", "ja", "zh", "hi"])

if st.button("Translate"):
    if text_to_translate:
        try:
            # LibreTranslate public API requires POST
            url = "https://libretranslate.de/translate" # Using .de mirror often more stable for free use or try .com
            # Actually, let's try a few known public instances or just the main one.
            # Main one: https://libretranslate.com/translate (often requires key or has captcha)
            # Let's try https://libretranslate.de/translate
            
            payload = {
                "q": text_to_translate,
                "source": "auto",
                "target": target_lang,
                "format": "text"
            }
            
            response = requests.post("https://libretranslate.de/translate", data=payload)
            
            if response.status_code == 200:
                data = response.json()
                st.success("Translation:")
                st.write(data['translatedText'])
            else:
                # Fallback to another instance if possible or show error
                st.error(f"Translation failed. Status: {response.status_code}. The public API might be busy.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text.")
