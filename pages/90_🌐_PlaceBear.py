import streamlit as st

st.set_page_config(page_title="PlaceBear", page_icon="🐻")

st.markdown("# 🐻 PlaceBear")
st.write("Generate placeholder bear images.")

col1, col2 = st.columns(2)
with col1:
    width = st.slider("Width", 100, 1000, 400)
with col2:
    height = st.slider("Height", 100, 1000, 300)

grayscale = st.checkbox("Grayscale")

if st.button("Generate Bear"):
    url = f"https://placebear.com/{'g/' if grayscale else ''}{width}/{height}"
    st.image(url, caption=f"Bear {width}x{height}")
    st.code(url)
