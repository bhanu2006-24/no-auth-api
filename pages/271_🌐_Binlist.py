import streamlit as st
import requests

st.set_page_config(page_title="Binlist", page_icon="💳")

st.markdown("# 💳 Binlist")
st.write("BIN/IIN Lookup.")

bin_num = st.text_input("First 6/8 digits of Card", "45717360")

if st.button("Lookup"):
    try:
        response = requests.get(f"https://lookup.binlist.net/{bin_num}", headers={'Accept-Version': '3'})
        if response.status_code == 200:
            data = response.json()
            st.write(f"**Scheme:** {data.get('scheme', '')}")
            st.write(f"**Type:** {data.get('type', '')}")
            st.write(f"**Bank:** {data.get('bank', {}).get('name', '')}")
            st.write(f"**Country:** {data.get('country', {}).get('name', '')}")
        else:
            st.error("Not Found or Limit Reached.")
    except Exception as e:
        st.error(f"Error: {e}")
