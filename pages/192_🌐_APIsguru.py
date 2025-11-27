import streamlit as st
import requests

st.set_page_config(page_title="APIs.guru", page_icon="🧘")

st.markdown("# 🧘 APIs.guru")
st.write("Wikipedia for Web APIs.")

if st.button("Get List"):
    try:
        response = requests.get("https://api.apis.guru/v2/providers.json")
        if response.status_code == 200:
            data = response.json()
            st.write(f"Total Providers: {len(data['data'])}")
            st.json(list(data['data'])[:20])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
