import streamlit as st
import requests

st.set_page_config(page_title="Nobel Prize", page_icon="🏅")
st.markdown("# 🏅 Nobel Prize")

category = st.selectbox("Category", ["phy", "che", "med", "lit", "pea", "eco"])
year = st.number_input("Year", 1901, 2023, 2020)

if st.button("Search"):
    try:
        response = requests.get(f"https://api.nobelprize.org/2.1/nobelPrizes?awardYear={year}&nobelPrizeCategory={category}")
        if response.status_code == 200:
            data = response.json()
            if 'nobelPrizes' in data:
                for prize in data['nobelPrizes']:
                    st.subheader(f"{prize['categoryFullName']['en']} ({prize['awardYear']})")
                    for laureate in prize['laureates']:
                        st.write(f"**{laureate['knownName']['en']}**")
                        st.write(laureate['motivation']['en'])
            else:
                st.warning("No prizes found.")
    except Exception as e:
        st.error(f"Error: {e}")
