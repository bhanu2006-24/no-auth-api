import streamlit as st
import requests

st.set_page_config(page_title="Random User", page_icon="🧑")

st.markdown("# 🧑 Random User Generator")
st.sidebar.header("Random User")
st.write(
    """This page generates a random user profile using the [Random User Generator API](https://randomuser.me/)."""
)

if st.button("Generate User"):
    try:
        response = requests.get("https://randomuser.me/api/")
        if response.status_code == 200:
            data = response.json()["results"][0]
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(data["picture"]["large"], width=200)
            
            with col2:
                st.subheader(f"{data['name']['title']} {data['name']['first']} {data['name']['last']}")
                st.write(f"**Email:** {data['email']}")
                st.write(f"**Phone:** {data['phone']}")
                st.write(f"**Location:** {data['location']['city']}, {data['location']['country']}")
                st.write(f"**Nationality:** {data['nat']}")
        else:
            st.error("Failed to fetch user. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
