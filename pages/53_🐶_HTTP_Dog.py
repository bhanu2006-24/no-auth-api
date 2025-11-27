import streamlit as st
import requests

st.set_page_config(page_title="HTTP Status Dogs", page_icon="🐶")

st.title("🐶 HTTP Status Dogs")
st.markdown("Get dogs representing HTTP status codes using [HTTP Dog](https://http.dog/).")

status_code = st.selectbox("Select HTTP Status Code", [
    100, 101, 102, 200, 201, 202, 203, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 308,
    400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 420, 421, 422, 423, 424, 425, 426, 429, 431, 444, 450, 451, 497, 498, 499,
    500, 501, 502, 503, 504, 506, 507, 508, 509, 510, 511, 521, 522, 523, 525, 599
])

if st.button("Show Dog"):
    url = f"https://http.dog/{status_code}.jpg"
    st.image(url, caption=f"HTTP {status_code}", use_column_width=True)
