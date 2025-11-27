import streamlit as st

st.set_page_config(page_title="Lorem Picsum", page_icon="📸")

st.markdown("# 📸 Lorem Picsum")
st.sidebar.header("Lorem Picsum")
st.write(
    """This page generates random placeholder photos using [Lorem Picsum](https://picsum.photos/)."""
)

width = st.slider("Width", 100, 800, 400)
height = st.slider("Height", 100, 800, 300)
grayscale = st.checkbox("Grayscale")
blur = st.slider("Blur Level", 0, 10, 0)

if st.button("Get Photo"):
    url = f"https://picsum.photos/{width}/{height}"
    params = []
    if grayscale:
        params.append("grayscale")
    if blur > 0:
        params.append(f"blur={blur}")
    
    if params:
        url += "?" + "&".join(params)
        
    st.image(url, caption=f"Random Photo ({width}x{height})")
