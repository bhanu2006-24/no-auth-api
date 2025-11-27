import streamlit as st
import requests

st.set_page_config(page_title="Makeup API", page_icon="💄")

st.markdown("# 💄 Makeup API")
st.sidebar.header("Makeup API")
st.write(
    """This page searches for cosmetic products using the [Makeup API](http://makeup-api.herokuapp.com/)."""
)

brand = st.selectbox("Select Brand", ["maybelline", "l'oreal", "covergirl", "revlon", "nyx", "elf"])

if st.button("Search Products"):
    try:
        response = requests.get(f"http://makeup-api.herokuapp.com/api/v1/products.json?brand={brand}")
        if response.status_code == 200:
            data = response.json()
            if data:
                st.success(f"Found {len(data)} products from {brand.capitalize()}:")
                # Show top 10
                for product in data[:10]:
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        if product["image_link"]:
                            st.image(product["image_link"], width=100)
                    with col2:
                        st.subheader(product["name"])
                        st.write(f"**Price:** {product['price_sign']}{product['price']}")
                        if product["product_link"]:
                            st.write(f"[Product Link]({product['product_link']})")
                    st.markdown("---")
            else:
                st.warning("No products found.")
        else:
            st.error("Failed to fetch products. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
