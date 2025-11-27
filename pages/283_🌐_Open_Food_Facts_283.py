import streamlit as st
import requests

st.set_page_config(page_title="Open Food Facts", page_icon="🥫")

st.markdown("# 🥫 Open Food Facts")

barcode = st.text_input("Barcode", "737628064502")

if st.button("Scan"):
    try:
        response = requests.get(f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json")
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 1:
                product = data['product']
                st.header(product.get('product_name', 'Unknown'))
                st.image(product.get('image_front_url', ''))
                st.write(f"**Brands:** {product.get('brands', '')}")
            else:
                st.error("Product not found.")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
