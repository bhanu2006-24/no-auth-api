import streamlit as st

st.set_page_config(page_title="DiceBear", page_icon="🎲")

st.markdown("# 🎲 DiceBear Avatars")
st.sidebar.header("DiceBear")
st.write(
    """This page generates random avatars using the [DiceBear API](https://www.dicebear.com/)."""
)

seed = st.text_input("Enter seed (name)", "Felix")
style = st.selectbox("Style", ["adventurer", "adventurer-neutral", "avataaars", "big-ears", "big-ears-neutral", "big-smile", "bottts", "croodles", "croodles-neutral", "fun-emoji", "icons", "identicon", "initials", "lorelei", "lorelei-neutral", "micah", "miniavs", "open-peeps", "personas", "pixel-art", "pixel-art-neutral", "shapes", "thumbs"])

if st.button("Generate Avatar"):
    url = f"https://api.dicebear.com/7.x/{style}/svg?seed={seed}"
    st.image(url, caption=f"{style} avatar for {seed}", width=200)
