import streamlit as st
import requests

st.set_page_config(page_title="Church Calendar", page_icon="⛪")

st.markdown("# ⛪ Church Calendar")
st.write("Catholic liturgical calendar.")

if st.button("Get Today's Calendar"):
    try:
        response = requests.get("http://calapi.inadiutorium.cz/api/v0/en/calendars/default/today")
        if response.status_code == 200:
            data = response.json()
            st.subheader(data["date"])
            st.write(f"**Season:** {data['season']}")
            st.write(f"**Celebrations:**")
            for cel in data['celebrations']:
                st.write(f"- {cel['title']} ({cel['colour']})")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
