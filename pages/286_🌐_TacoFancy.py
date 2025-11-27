import streamlit as st
import requests

st.set_page_config(page_title="TacoFancy", page_icon="🌮")

st.markdown("# 🌮 TacoFancy")
st.write("Random taco recipes.")

if st.button("Get Taco"):
    try:
        response = requests.get("http://taco-randomizer.herokuapp.com/random/")
        if response.status_code == 200:
            data = response.json()
            st.header(data.get('base_layer', {}).get('name', 'Taco'))
            st.write(f"**Shell:** {data.get('shell', {}).get('name', '')}")
            st.write(f"**Seasoning:** {data.get('seasoning', {}).get('name', '')}")
            st.write(f"**Condiment:** {data.get('condiment', {}).get('name', '')}")
            st.markdown(data.get('base_layer', {}).get('recipe', ''))
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
