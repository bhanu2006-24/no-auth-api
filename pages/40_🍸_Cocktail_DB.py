import streamlit as st
import requests

st.set_page_config(page_title="The Cocktail DB", page_icon="🍸")

st.markdown("# 🍸 The Cocktail DB")
st.sidebar.header("The Cocktail DB")
st.write(
    """This page fetches a random cocktail recipe using [TheCocktailDB](https://www.thecocktaildb.com/)."""
)

if st.button("Get Cocktail"):
    try:
        response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/random.php")
        if response.status_code == 200:
            data = response.json()["drinks"][0]
            
            st.header(data["strDrink"])
            
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(data["strDrinkThumb"], use_column_width=True)
            
            with col2:
                st.subheader("Ingredients")
                for i in range(1, 16):
                    ingredient = data[f"strIngredient{i}"]
                    measure = data[f"strMeasure{i}"]
                    if ingredient:
                        st.write(f"- {measure if measure else ''} {ingredient}")
                
                st.subheader("Instructions")
                st.write(data["strInstructions"])
                
                st.write(f"**Glass:** {data['strGlass']}")
                st.write(f"**Category:** {data['strCategory']}")
        else:
            st.error("Failed to fetch cocktail. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
