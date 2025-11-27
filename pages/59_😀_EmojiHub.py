import streamlit as st
import requests

st.set_page_config(page_title="Emoji Hub", page_icon="😀")

st.title("😀 Emoji Hub")
st.markdown("Get random emojis using [EmojiHub](https://emojihub.yurace.pro/).")

if st.button("Get Random Emoji"):
    try:
        response = requests.get("https://emojihub.yurace.pro/api/random")
        if response.status_code == 200:
            data = response.json()
            st.header(data['htmlCode'][0]) # Displaying the emoji using HTML code
            st.markdown(data['htmlCode'][0], unsafe_allow_html=True) # This might render as text in markdown, let's try st.html or just big text
            
            st.write(f"**Name:** {data['name']}")
            st.write(f"**Category:** {data['category']}")
            st.write(f"**Group:** {data['group']}")
            st.code(data['htmlCode'][0], language="html")
        else:
            st.error("Failed to fetch emoji.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
