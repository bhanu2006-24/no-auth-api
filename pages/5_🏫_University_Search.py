import streamlit as st
import requests

st.set_page_config(page_title="University Search", page_icon="🏫")

st.markdown("# 🏫 University Search")
st.sidebar.header("University Search")
st.write(
    """This page searches for universities in a specific country using the [Hipolabs University API](http://universities.hipolabs.com/)."""
)

country = st.text_input("Enter a country", "United States")

if st.button("Search Universities"):
    if country:
        try:
            response = requests.get(f"http://universities.hipolabs.com/search?country={country}")
            if response.status_code == 200:
                data = response.json()
                if data:
                    st.success(f"Found {len(data)} universities in {country}:")
                    # Display first 20 results to avoid overwhelming the page
                    for uni in data[:20]:
                        st.write(f"- [{uni['name']}]({uni['web_pages'][0]})")
                    if len(data) > 20:
                        st.info(f"...and {len(data) - 20} more.")
                else:
                    st.warning(f"No universities found in {country}.")
            else:
                st.error("Failed to fetch data. The API might be down.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a country.")
