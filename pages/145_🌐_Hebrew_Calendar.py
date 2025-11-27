import streamlit as st
import requests

st.set_page_config(page_title="Hebrew Calendar", page_icon="🕎")

st.markdown("# 🕎 Hebrew Calendar")
st.write("Convert dates to Hebrew calendar.")

if st.button("Get Today's Hebrew Date"):
    try:
        response = requests.get("https://www.hebcal.com/converter?cfg=json&gy=2023&gm=10&gd=25&g2h=1") # Using fixed date for demo or current
        # Better: use current date
        import datetime
        now = datetime.datetime.now()
        url = f"https://www.hebcal.com/converter?cfg=json&gy={now.year}&gm={now.month}&gd={now.day}&g2h=1"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            st.header(data["hebrew"])
            st.write(f"**Year:** {data['hy']}")
            st.write(f"**Month:** {data['hm']}")
            st.write(f"**Day:** {data['hd']}")
            st.write(f"**Events:** {', '.join(data['events'])}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
