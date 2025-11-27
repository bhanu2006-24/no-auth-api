import streamlit as st

st.set_page_config(page_title="Pixel Encounter", page_icon="👾")

st.markdown("# 👾 Pixel Encounter Monsters")
st.write("Generate random pixel monsters.")

width = st.slider("Width", 100, 500, 200)

if st.button("Generate Monster"):
    # Using a random ID to force refresh
    import random
    rand_id = random.randint(1, 10000)
    url = f"https://pixelencounter.com/api/basic/monsters/random/png?width={width}&_={rand_id}"
    st.image(url, caption="Pixel Monster")
