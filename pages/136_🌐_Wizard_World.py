import streamlit as st
import requests

st.set_page_config(page_title="Wizard World", page_icon="🧙")

st.markdown("# 🧙 Wizard World (Harry Potter)")
st.write("Explore spells from the Wizarding World.")

if st.button("Get Random Spell"):
    try:
        response = requests.get("https://wizard-world-api.herokuapp.com/Spells")
        if response.status_code == 200:
            spells = response.json()
            if spells:
                import random
                spell = random.choice(spells)
                st.header(spell['name'])
                st.write(f"**Incantation:** {spell.get('incantation', 'Unknown')}")
                st.write(f"**Effect:** {spell.get('effect', 'Unknown')}")
                st.write(f"**Type:** {spell.get('type', 'Unknown')}")
                st.write(f"**Light:** {spell.get('light', 'None')}")
    except Exception as e:
        st.error(f"Error: {e}")
