import streamlit as st
import requests

st.set_page_config(page_title="Thirukkural", page_icon="📜")

st.markdown("# 📜 Thirukkural")
st.write("Classic Tamil text.")

if st.button("Get Random Kural"):
    try:
        response = requests.get("https://api-thirukkural.vercel.app/api?num=rnd")
        if response.status_code == 200:
            data = response.json()
            st.subheader(f"Kural {data.get('number')}")
            st.markdown(f"**Tamil:** {data.get('line1')}\n{data.get('line2')}")
            st.markdown(f"**English:** {data.get('eng')}")
            st.write(f"**Explanation:** {data.get('eng_exp')}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
