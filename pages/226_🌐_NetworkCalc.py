import streamlit as st
import requests

st.set_page_config(page_title="NetworkCalc", page_icon="🧮")

st.markdown("# 🧮 NetworkCalc")
st.write("Subnet calculator.")

ip = st.text_input("IP/CIDR", "192.168.1.1/24")

if st.button("Calculate"):
    try:
        response = requests.get(f"https://networkcalc.com/api/ip/{ip}")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
