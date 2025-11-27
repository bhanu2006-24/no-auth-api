import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="URLhaus", page_icon="🛡️")

st.markdown("# 🛡️ URLhaus Recent Malware URLs")
st.write("Recent malware URLs identified by URLhaus.")

if st.button("Fetch Recent URLs"):
    try:
        response = requests.get("https://urlhaus-api.abuse.ch/v1/urls/recent/")
        if response.status_code == 200:
            data = response.json()
            if data["query_status"] == "ok":
                urls = data["urls"]
                df = pd.DataFrame(urls)
                st.dataframe(df[["id", "url_status", "date_added", "url", "reporter", "threat", "tags"]])
            else:
                st.error("Query failed.")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
