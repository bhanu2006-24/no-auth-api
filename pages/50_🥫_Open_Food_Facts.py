import streamlit as st
import requests

st.set_page_config(page_title="Open Food Facts", page_icon="🥫")

st.markdown("# 🥫 Open Food Facts")
st.sidebar.header("Open Food Facts")
st.write(
    """This page fetches food product information using the [Open Food Facts API](https://world.openfoodfacts.org/)."""
)

barcode = st.text_input("Enter Product Barcode", "737628064502") # Example: Rice Noodles

if st.button("Get Product Info"):
    if barcode:
        try:
            response = requests.get(f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json")
            if response.status_code == 200:
                data = response.json()
                if data["status"] == 1:
                    product = data["product"]
                    st.header(product.get("product_name", "Unknown Product"))
                    
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        if "image_front_url" in product:
                            st.image(product["image_front_url"], use_column_width=True)
                    
                    with col2:
                        st.write(f"**Brand:** {product.get('brands', 'Unknown')}")
                        st.write(f"**Quantity:** {product.get('quantity', 'Unknown')}")
                        st.write(f"**Categories:** {product.get('categories', 'Unknown')}")
                        
                        if "nutriments" in product:
                            st.subheader("Nutrition (per 100g)")
                            nutriments = product["nutriments"]
                            st.write(f"- Energy: {nutriments.get('energy-kcal_100g', 'N/A')} kcal")
                            st.write(f"- Fat: {nutriments.get('fat_100g', 'N/A')} g")
                            st.write(f"- Carbs: {nutriments.get('carbohydrates_100g', 'N/A')} g")
                            st.write(f"- Sugars: {nutriments.get('sugars_100g', 'N/A')} g")
                            st.write(f"- Protein: {nutriments.get('proteins_100g', 'N/A')} g")
                            st.write(f"- Salt: {nutriments.get('salt_100g', 'N/A')} g")
                else:
                    st.warning("Product not found.")
            else:
                st.error("Failed to fetch product. The API might be down.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a barcode.")
