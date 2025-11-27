import streamlit as st
import requests

st.set_page_config(page_title="Razorpay IFSC", page_icon="🏦")

st.markdown("# 🏦 Razorpay IFSC")
st.write("Indian Financial System Code lookup.")

ifsc = st.text_input("IFSC Code", "SBIN0000300")

if st.button("Lookup"):
    try:
        response = requests.get(f"https://ifsc.razorpay.com/{ifsc}")
        if response.status_code == 200:
            data = response.json()
            st.write(f"**Bank:** {data['BANK']}")
            st.write(f"**Branch:** {data['BRANCH']}")
            st.write(f"**Address:** {data['ADDRESS']}")
            st.write(f"**City:** {data['CITY']}")
        else:
            st.error("Invalid Code.")
    except Exception as e:
        st.error(f"Error: {e}")
