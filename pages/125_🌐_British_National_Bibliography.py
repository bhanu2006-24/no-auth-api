import streamlit as st

st.set_page_config(page_title="British National Bibliography", page_icon="🇬🇧")

st.markdown("# 🇬🇧 British National Bibliography")
st.write("Linked Open Data from the British Library.")

st.info("This API uses SPARQL which is complex for a simple demo. Visit the portal below.")
st.markdown("[BNB Linked Data](http://bnb.data.bl.uk/)")
