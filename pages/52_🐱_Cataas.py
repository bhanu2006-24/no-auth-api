import streamlit as st
import requests
from io import BytesIO

st.set_page_config(page_title="Cat as a Service", page_icon="🐱")

st.title("🐱 Cat as a Service (Cataas)")
st.markdown("Fetch random cats, cats with text, and more using [Cataas](https://cataas.com/).")

tab1, tab2 = st.tabs(["Random Cat", "Cat with Text"])

with tab1:
    if st.button("Get Random Cat"):
        try:
            # Timestamp to avoid caching
            import time
            timestamp = int(time.time())
            image_url = f"https://cataas.com/cat?t={timestamp}"
            st.image(image_url, caption="Random Cat", use_column_width=True)
        except Exception as e:
            st.error(f"An error occurred: {e}")

with tab2:
    text = st.text_input("Enter text to say:", "Hello Streamlit")
    if st.button("Get Cat with Text"):
        if text:
            try:
                # We need to fetch the image content because streamlit image() with URL might not handle the dynamic generation well if not cached properly, 
                # but usually it's fine. However, for 'says', it's a generated image.
                url = f"https://cataas.com/cat/says/{text}"
                response = requests.get(url)
                if response.status_code == 200:
                    st.image(BytesIO(response.content), caption=f"Cat says: {text}", use_column_width=True)
                else:
                    st.error("Failed to generate cat meme.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter some text.")
