import streamlit as st
import requests

st.set_page_config(page_title="WallstreetBets", page_icon="🚀")

st.markdown("# 🚀 WallstreetBets")
st.write("Trending stocks.")

if st.button("Get Trending"):
    try:
        response = requests.get("https://tradestie.com/api/v1/apps/reddit")
        if response.status_code == 200:
            data = response.json()
            for stock in data[:10]:
                st.metric(stock['ticker'], f"{stock['sentiment']} Sentiment", f"Comments: {stock['no_of_comments']}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
