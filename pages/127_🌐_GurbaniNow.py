import streamlit as st
import requests

st.set_page_config(page_title="GurbaniNow", page_icon="🙏")

st.markdown("# 🙏 GurbaniNow")
st.write("Get the daily Hukamnama.")

if st.button("Get Hukamnama"):
    try:
        response = requests.get("https://api.gurbaninow.com/v2/hukamnama/today")
        if response.status_code == 200:
            data = response.json()
            hukam = data.get("hukamnama", [])
            if hukam:
                line = hukam[0]["line"]
                st.markdown(f"### {line['gurmukhi']['unicode']}")
                st.markdown(f"*{line['translation']['english']['default']}*")
            else:
                st.warning("No data available.")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
