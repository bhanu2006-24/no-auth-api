import streamlit as st
import requests

st.set_page_config(page_title="The Meal DB", page_icon="🍲")

st.markdown("# 🍲 The Meal DB")
st.sidebar.header("The Meal DB")
st.write(
    """This page fetches a random meal recipe using [TheMealDB](https://www.themealdb.com/)."""
)

if st.button("Get Meal"):
    try:
        response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
        if response.status_code == 200:
            data = response.json()["meals"][0]
            
            st.header(data["strMeal"])
            st.caption(f"Category: {data['strCategory']} | Area: {data['strArea']}")
            
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(data["strMealThumb"], use_column_width=True)
            
            with col2:
                st.subheader("Ingredients")
                for i in range(1, 21):
                    ingredient = data[f"strIngredient{i}"]
                    measure = data[f"strMeasure{i}"]
                    if ingredient and ingredient.strip():
                        st.write(f"- {measure if measure else ''} {ingredient}")
                
                st.subheader("Instructions")
                st.write(data["strInstructions"])
                
                if data["strYoutube"]:
                    st.write(f"[Watch on YouTube]({data['strYoutube']})")
        else:
            st.error("Failed to fetch meal. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
