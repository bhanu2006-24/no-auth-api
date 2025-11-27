import streamlit as st
import requests

st.set_page_config(page_title="MC Status", page_icon="⛏️")
st.markdown("# ⛏️ Minecraft Server Status")

ip = st.text_input("Server IP", "mc.hypixel.net")

if st.button("Check"):
    try:
        response = requests.get(f"https://api.mcsrvstat.us/2/{ip}")
        if response.status_code == 200:
            data = response.json()
            if data['online']:
                st.success("Online")
                st.write(f"**Players:** {data['players']['online']}/{data['players']['max']}")
                st.write(f"**MOTD:** {', '.join(data['motd']['clean'])}")
            else:
                st.error("Offline")
    except Exception as e:
        st.error(f"Error: {e}")
