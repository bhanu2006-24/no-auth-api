import streamlit as st
import requests

st.set_page_config(page_title="CityBikes", page_icon="🚲")

st.title("🚲 CityBikes")
st.markdown("Find bike sharing networks using [CityBikes API](http://api.citybik.es/v2/).")

country_code = st.text_input("Enter Country Code (e.g., US, FR, GB, IN)", "US").upper()

if st.button("Find Networks"):
    try:
        response = requests.get("http://api.citybik.es/v2/networks")
        if response.status_code == 200:
            data = response.json()
            networks = data['networks']
            
            filtered_networks = [net for net in networks if net['location']['country'] == country_code]
            
            if filtered_networks:
                st.success(f"Found {len(filtered_networks)} networks in {country_code}.")
                
                for net in filtered_networks:
                    with st.expander(f"{net['name']} ({net['location']['city']})"):
                        st.write(f"**City:** {net['location']['city']}")
                        st.write(f"**Company:** {', '.join(net.get('company', [])) if isinstance(net.get('company'), list) else net.get('company', 'N/A')}")
                        st.markdown(f"[More Info](http://api.citybik.es{net['href']})")
            else:
                st.warning(f"No networks found for country code: {country_code}")
        else:
            st.error("Failed to fetch networks.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
