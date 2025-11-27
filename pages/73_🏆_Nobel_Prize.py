import streamlit as st
import requests

st.set_page_config(page_title="Nobel Prizes", page_icon="🏆")

st.title("🏆 Nobel Prizes")
st.markdown("Search for Nobel Prize laureates using the [Nobel Prize API](https://www.nobelprize.org/).")

year = st.number_input("Enter Year", min_value=1901, max_value=2023, value=2023)
category = st.selectbox("Select Category", ["physics", "chemistry", "medicine", "literature", "peace", "economics"])

if st.button("Get Winners"):
    try:
        response = requests.get(f"https://api.nobelprize.org/v1/prize.json?year={year}&category={category}")
        if response.status_code == 200:
            data = response.json()
            prizes = data.get('prizes', [])
            
            if prizes:
                for prize in prizes:
                    st.subheader(f"{prize['category'].capitalize()} ({prize['year']})")
                    laureates = prize.get('laureates', [])
                    for laureate in laureates:
                        firstname = laureate.get('firstname', '')
                        surname = laureate.get('surname', '')
                        motivation = laureate.get('motivation', 'No motivation available.')
                        st.write(f"**{firstname} {surname}**")
                        st.caption(motivation)
            else:
                st.warning("No prizes found for this criteria.")
        else:
            st.error("Failed to fetch data.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
