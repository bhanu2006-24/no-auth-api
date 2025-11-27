import streamlit as st
import requests

st.set_page_config(page_title="Waifu.im", page_icon="💃")

st.markdown("# 💃 Waifu.im")
st.write("Search for Waifu images.")

is_nsfw = st.checkbox("NSFW (Enable at your own risk)", value=False)
tag = st.selectbox("Tag", ["maid", "waifu", "marin-kitagawa", "mori-calliope", "raiden-shogun", "oppai", "selfies", "uniform"])

if st.button("Get Waifu"):
    try:
        params = {"is_nsfw": str(is_nsfw).lower(), "included_tags": tag}
        response = requests.get("https://api.waifu.im/search", params=params)
        if response.status_code == 200:
            data = response.json()
            if data["images"]:
                img = data["images"][0]
                st.image(img["url"], caption=f"Tag: {tag}", use_column_width=True)
                st.markdown(f"[Source]({img['source']})")
            else:
                st.warning("No images found.")
        else:
            st.error(f"API Error: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {e}")
