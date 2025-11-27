import streamlit as st

st.set_page_config(page_title="Crafatar", page_icon="⛏️")

st.markdown("# ⛏️ Crafatar")
st.write("Minecraft avatars.")

uuid = st.text_input("UUID", "853c80ef3c3749fdaa49938b674adae6")

if st.button("Get Avatar"):
    col1, col2 = st.columns(2)
    with col1:
        st.image(f"https://crafatar.com/avatars/{uuid}", caption="Avatar")
    with col2:
        st.image(f"https://crafatar.com/renders/body/{uuid}", caption="Body")
