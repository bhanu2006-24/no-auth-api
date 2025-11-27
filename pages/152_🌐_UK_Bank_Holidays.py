import streamlit as st
import requests

st.set_page_config(page_title="UK Bank Holidays", page_icon="🇬🇧")

st.markdown("# 🇬🇧 UK Bank Holidays")
st.write("Upcoming bank holidays in the UK.")

if st.button("Fetch Holidays"):
    try:
        response = requests.get("https://www.gov.uk/bank-holidays.json")
        if response.status_code == 200:
            data = response.json()
            for region, details in data.items():
                with st.expander(details['division']):
                    for event in details['events'][:5]: # Show next 5
                        st.write(f"**{event['date']}:** {event['title']}")
                        if event.get('notes'):
                            st.caption(event['notes'])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
