import streamlit as st
import requests

st.set_page_config(page_title="Harry Potter Characters", page_icon="🧙‍♂️")

st.title("🧙‍♂️ Harry Potter Characters")
st.markdown("Explore characters from the Harry Potter universe using [HP-API](https://hp-api.herokuapp.com/).")

if st.button("Load Characters"):
    try:
        response = requests.get("https://hp-api.herokuapp.com/api/characters")
        if response.status_code == 200:
            data = response.json()
            # Filter characters with images
            chars_with_images = [c for c in data if c.get('image')]
            
            if chars_with_images:
                import random
                # Show 5 random characters
                selected = random.sample(chars_with_images, min(5, len(chars_with_images)))
                
                for char in selected:
                    with st.expander(f"{char['name']}"):
                        col1, col2 = st.columns([1, 2])
                        with col1:
                            st.image(char['image'], width=150)
                        with col2:
                            st.write(f"**House:** {char.get('house', 'Unknown')}")
                            st.write(f"**Actor:** {char.get('actor', 'Unknown')}")
                            st.write(f"**Ancestry:** {char.get('ancestry', 'Unknown')}")
            else:
                st.warning("No characters with images found.")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
