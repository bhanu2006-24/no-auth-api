import streamlit as st

st.set_page_config(page_title="PHP Noise", page_icon="🌫️")

st.markdown("# 🌫️ PHP Noise Generator")
st.write("Generate noise background images.")

r = st.slider("Red", 0, 255, 100)
g = st.slider("Green", 0, 255, 100)
b = st.slider("Blue", 0, 255, 100)
tiles = st.slider("Tiles", 1, 50, 10)

if st.button("Generate Noise"):
    url = f"http://php-noise.com/noise.php?r={r}&g={g}&b={b}&tiles={tiles}&json"
    # The API returns JSON with a base64 uri or just the image if no json param
    # Let's use direct image url
    img_url = f"http://php-noise.com/noise.php?r={r}&g={g}&b={b}&tiles={tiles}"
    st.image(img_url, caption="Generated Noise")
    st.code(img_url)
