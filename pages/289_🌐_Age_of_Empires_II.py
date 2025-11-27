import streamlit as st
import requests

st.set_page_config(page_title="Age of Empires II", page_icon="⚔️")

st.markdown("# ⚔️ Age of Empires II")

if st.button("Get Civilizations"):
    try:
        response = requests.get("https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations")
        if response.status_code == 200:
            data = response.json()
            for civ in data['civilizations'][:5]:
                st.subheader(civ['name'])
                st.write(f"**Expansion:** {civ['expansion']}")
                st.write(f"**Bonus:** {', '.join(civ['civilization_bonus'])}")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
