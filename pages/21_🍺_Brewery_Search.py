import streamlit as st
import requests

st.set_page_config(page_title="Brewery Search", page_icon="🍺")

st.markdown("# 🍺 Brewery Search")
st.sidebar.header("Brewery Search")
st.write(
    """This page searches for breweries using the [Open Brewery DB API](https://www.openbrewerydb.org/)."""
)

city = st.text_input("Enter a city", "San Diego")

if st.button("Search Breweries"):
    if city:
        try:
            response = requests.get(f"https://api.openbrewerydb.org/breweries?by_city={city}&per_page=10")
            if response.status_code == 200:
                data = response.json()
                if data:
                    st.success(f"Found {len(data)} breweries in {city}:")
                    for brewery in data:
                        st.subheader(brewery["name"])
                        st.write(f"**Type:** {brewery['brewery_type']}")
                        st.write(f"**Address:** {brewery['street']}, {brewery['city']}, {brewery['state']}")
                        if brewery["website_url"]:
                            st.write(f"[Website]({brewery['website_url']})")
                        st.markdown("---")
                else:
                    st.warning(f"No breweries found in {city}.")
            else:
                st.error("Failed to fetch breweries. The API might be down.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a city.")
