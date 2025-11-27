import streamlit as st
import requests

st.set_page_config(page_title="Bored API", page_icon="🥱")

st.markdown("# 🥱 Bored API")
st.sidebar.header("Bored API")
st.write(
    """This page suggests random activities to do using the [Bored API](https://www.boredapi.com/)."""
)

type_option = st.selectbox("Activity Type", ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

if st.button("Get Activity"):
    try:
        response = requests.get(f"https://www.boredapi.com/api/activity?type={type_option}")
        if response.status_code == 200:
            data = response.json()
            st.success(data["activity"])
            st.write(f"**Participants:** {data['participants']}")
            st.write(f"**Price:** {data['price']}")
            if data["link"]:
                st.write(f"[Link]({data['link']})")
        else:
            st.error("Failed to fetch activity. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
