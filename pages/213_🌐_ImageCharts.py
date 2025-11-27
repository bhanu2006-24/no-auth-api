import streamlit as st

st.set_page_config(page_title="Image-Charts", page_icon="📊")

st.markdown("# 📊 Image-Charts")
st.write("Generate charts via URL.")

chart_type = st.selectbox("Type", ["bvg", "p3", "lc"])
data = st.text_input("Data (comma separated)", "10,20,30,40,50")

if st.button("Generate"):
    url = f"https://image-charts.com/chart?cht={chart_type}&chd=t:{data}&chs=500x300"
    st.image(url, caption="Generated Chart")
    st.code(url)
