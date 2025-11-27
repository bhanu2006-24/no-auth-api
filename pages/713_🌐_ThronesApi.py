import streamlit as st
import requests

st.set_page_config(page_title="Thrones API", page_icon="🐉")

st.title("🐉 Game of Thrones Characters")
st.markdown("Explore characters from Game of Thrones using [ThronesAPI](https://thronesapi.com/).")

if st.button("Load Characters"):
    try:
        response = requests.get("https://thronesapi.com/api/v2/Characters")
        if response.status_code == 200:
            data = response.json()
            
            import random
            # Show 5 random characters
            selected = random.sample(data, min(5, len(data)))
            
            for char in selected:
                with st.expander(f"{char['fullName']}"):
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        st.image(char['imageUrl'], width=150)
                    with col2:
                        st.write(f"**Title:** {char.get('title', 'Unknown')}")
                        st.write(f"**Family:** {char.get('family', 'Unknown')}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
