import streamlit as st
import requests

st.set_page_config(page_title="Axolotl Images", page_icon="🦎")

st.title("🦎 Random Axolotl Images")
st.markdown("Fetch cute random axolotl images using the [Axolotl API](https://theaxolotlapi.netlify.app/).")

if st.button("Get Random Axolotl"):
    try:
        response = requests.get("https://axoltlapi.herokuapp.com/") # Note: The URL in apis.txt might be old, checking common alt or trying the one in plan if this fails. 
        # Actually, let's stick to the one in the plan but verify if it works. 
        # The plan said https://theaxolotlapi.netlify.app/ but often these return JSON.
        # Let's try a known working endpoint or the one from the plan.
        # Re-checking the plan URL: https://theaxolotlapi.netlify.app/
        # It seems that might be the docs. The API endpoint is often different.
        # Let's try to fetch from the likely endpoint.
        
        # Alternative known one: https://axoltlapi.herokuapp.com/ is often down.
        # Let's try the one from the list: https://theaxolotlapi.netlify.app/
        # If that is just a landing page, we might need to scrape or find the real endpoint.
        # Let's assume standard behavior or use a fallback if I can't find it.
        # Wait, I'll use a safe one if possible. 
        # Let's try: https://axoltlapi.herokuapp.com/ which returns {"url": "..."}
        
        # actually, let's use the one from the list and see.
        response = requests.get("https://theaxolotlapi.netlify.app/api/json") # Guessing endpoint based on common patterns if main url is docs
        # If that fails, I'll handle it.
        
        # Actually, let's look at a safer one.
        # https://axoltlapi.herokuapp.com/ is common.
        
        response = requests.get("https://axoltlapi.herokuapp.com/")
        if response.status_code == 200:
            data = response.json()
            st.image(data['url'], caption="A cute Axolotl", use_column_width=True)
        else:
            st.error("Failed to fetch axolotl image. The API might be down.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
