import streamlit as st

st.set_page_config(page_title="RoboHash", page_icon="🤖")

st.markdown("# 🤖 RoboHash Avatars")
st.sidebar.header("RoboHash")
st.write(
    """This page generates unique robot avatars from text using the [RoboHash API](https://robohash.org/)."""
)

text = st.text_input("Enter text to generate avatar", "Streamlit")
set_type = st.selectbox("Avatar Set", ["set1 (Robots)", "set2 (Monsters)", "set3 (Disembodied Heads)", "set4 (Kittens)", "set5 (Humans)"])

if st.button("Generate Avatar"):
    if text:
        set_num = set_type.split(" ")[0]
        url = f"https://robohash.org/{text}?set={set_num}"
        st.image(url, caption=f"Avatar for '{text}'", width=300)
    else:
        st.warning("Please enter some text.")
