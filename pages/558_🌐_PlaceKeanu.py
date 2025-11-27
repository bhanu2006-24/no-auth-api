import streamlit as st

st.set_page_config(page_title="PlaceKeanu", page_icon="🕴️")

st.title("🕴️ PlaceKeanu")
st.markdown("Get placeholder images of Keanu Reeves using [PlaceKeanu](https://placekeanu.com/).")

col1, col2 = st.columns(2)
with col1:
    width = st.slider("Width", 100, 1000, 500)
with col2:
    height = st.slider("Height", 100, 1000, 400)

options = st.multiselect("Options", ["g (Grayscale)", "y (Young)"])

if st.button("Get Keanu"):
    # URL format: https://placekeanu.com/[options]/width/height
    # options: /g or /y or /gy
    
    opts = ""
    if "g (Grayscale)" in options: opts += "g"
    if "y (Young)" in options: opts += "y"
    
    url = f"https://placekeanu.com/{opts}/{width}/{height}".replace("//", "/")
    # Fix double slash if opts is empty but we have /width
    # Actually placekeanu format is https://placekeanu.com/[width]/[height]/[options] or https://placekeanu.com/[width]/[height]
    # Wait, docs say: https://placekeanu.com/[width]/[height]/[y|g]
    
    url = f"https://placekeanu.com/{width}/{height}"
    if opts:
        url += f"/{opts}"
        
    st.image(url, caption="Keanu Reeves", use_column_width=True)
    st.code(url)
