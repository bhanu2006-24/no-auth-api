import streamlit as st
import requests

st.set_page_config(page_title="FBI Wanted", page_icon="👮")
st.markdown("# 👮 FBI Wanted")

if st.button("Get List"):
    try:
        response = requests.get("https://api.fbi.gov/wanted/v1/list")
        if response.status_code == 200:
            data = response.json()
            for item in data['items'][:5]:
                st.subheader(item['title'])
                if item['images']:
                    st.image(item['images'][0]['original'])
                st.write(item.get('description', ''))
    except Exception as e:
        st.error(f"Error: {e}")
