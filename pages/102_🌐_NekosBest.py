import streamlit as st
import requests

st.set_page_config(page_title="Nekos.best", page_icon="😻")

st.markdown("# 😻 Nekos.best")
st.sidebar.header("Nekos.best")
st.write("Best Neko images and GIFs.")

category = st.selectbox("Category", ["neko", "kitsune", "husbando", "waifu"])

if st.button("Get Image"):
    try:
        response = requests.get(f"https://nekos.best/api/v2/{category}")
        if response.status_code == 200:
            data = response.json()
            result = data["results"][0]
            st.image(result["url"], caption=f"Artist: {result['artist_name']}", use_column_width=True)
            st.markdown(f"[Source]({result['source_url']})")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
