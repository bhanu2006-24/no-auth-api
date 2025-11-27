import streamlit as st
import requests

def fix_placekeanu():
    code = '''import streamlit as st

st.set_page_config(page_title="PlaceKeanu", page_icon="🕴️")

st.title("🕴️ PlaceKeanu")
st.markdown("Get placeholder images of Keanu Reeves using [PlaceKeanu](https://placekeanu.com/).")

col1, col2 = st.columns(2)
with col1:
    width = st.slider("Width", 100, 1000, 500)
with col2:
    height = st.slider("Height", 100, 1000, 400)

options = st.multiselect("Options", ["g (Grayscale)", "y (Young)"])

if st.button("Get Keanu"):
    # URL format: https://placekeanu.com/[options]/width/height
    # options: /g or /y or /gy
    
    opts = ""
    if "g (Grayscale)" in options: opts += "g"
    if "y (Young)" in options: opts += "y"
    
    url = f"https://placekeanu.com/{opts}/{width}/{height}".replace("//", "/")
    # Fix double slash if opts is empty but we have /width
    # Actually placekeanu format is https://placekeanu.com/[width]/[height]/[options] or https://placekeanu.com/[width]/[height]
    # Wait, docs say: https://placekeanu.com/[width]/[height]/[y|g]
    
    url = f"https://placekeanu.com/{width}/{height}"
    if opts:
        url += f"/{opts}"
        
    st.image(url, caption="Keanu Reeves", use_column_width=True)
    st.code(url)
'''
    with open('pages/558_🌐_PlaceKeanu.py', 'w') as f:
        f.write(code)

def fix_biriyani():
    code = '''import streamlit as st
import requests

st.set_page_config(page_title="Biriyani As A Service", page_icon="🍛")

st.title("🍛 Biriyani As A Service")
st.markdown("Get random biriyani images using [Biriyani As A Service](https://biriyani.asad.pro/).")

if st.button("Get Biriyani"):
    try:
        response = requests.get("https://biriyani.asad.pro/api/image")
        if response.status_code == 200:
            data = response.json()
            st.image(data["image"], caption="Biriyani Time!", use_column_width=True)
        else:
            st.error("Failed to fetch biriyani.")
    except Exception as e:
        st.error(f"Error: {e}")
'''
    with open('pages/536_🌐_Biriyani_As_A_Service.py', 'w') as f:
        f.write(code)

def fix_vadivelu():
    code = '''import streamlit as st
import requests

st.set_page_config(page_title="Vadivelu HTTP Codes", page_icon="🎭")

st.title("🎭 Vadivelu HTTP Codes")
st.markdown("Get Vadivelu reactions for HTTP status codes using [Vadivelu JSON](https://vadivelu.asad.pro/).")

code = st.number_input("HTTP Status Code", min_value=100, max_value=599, value=200)

if st.button("Get Reaction"):
    try:
        # The API seems to be https://vadivelu.asad.pro/api/id/:id
        # Or maybe just images?
        # Let's try to find the image URL pattern or fetch JSON
        # Docs: https://vadivelu.asad.pro/
        # It says "GET /api/http/:code"
        
        url = f"https://vadivelu.asad.pro/api/http/{code}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            st.image(data["image"], caption=f"Status {code}", use_column_width=True)
        else:
            st.error("Reaction not found for this code.")
    except Exception as e:
        st.error(f"Error: {e}")
'''
    with open('pages/552_🌐_Vadivelu_HTTP_Codes.py', 'w') as f:
        f.write(code)

def fix_harry_potter():
    code = '''import streamlit as st
import requests

st.set_page_config(page_title="Harry Potter Characters", page_icon="🧙‍♂️")

st.title("🧙‍♂️ Harry Potter Characters")
st.markdown("Explore characters from the Harry Potter universe using [HP-API](https://hp-api.herokuapp.com/).")

if st.button("Load Characters"):
    try:
        response = requests.get("https://hp-api.herokuapp.com/api/characters")
        if response.status_code == 200:
            data = response.json()
            # Filter characters with images
            chars_with_images = [c for c in data if c.get('image')]
            
            if chars_with_images:
                import random
                # Show 5 random characters
                selected = random.sample(chars_with_images, min(5, len(chars_with_images)))
                
                for char in selected:
                    with st.expander(f"{char['name']}"):
                        col1, col2 = st.columns([1, 2])
                        with col1:
                            st.image(char['image'], width=150)
                        with col2:
                            st.write(f"**House:** {char.get('house', 'Unknown')}")
                            st.write(f"**Actor:** {char.get('actor', 'Unknown')}")
                            st.write(f"**Ancestry:** {char.get('ancestry', 'Unknown')}")
            else:
                st.warning("No characters with images found.")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
'''
    with open('pages/698_🌐_Harry_Potter_Charactes.py', 'w') as f:
        f.write(code)

def fix_thrones():
    code = '''import streamlit as st
import requests

st.set_page_config(page_title="Thrones API", page_icon="🐉")

st.title("🐉 Game of Thrones Characters")
st.markdown("Explore characters from Game of Thrones using [ThronesAPI](https://thronesapi.com/).")

if st.button("Load Characters"):
    try:
        response = requests.get("https://thronesapi.com/api/v2/Characters")
        if response.status_code == 200:
            data = response.json()
            
            import random
            # Show 5 random characters
            selected = random.sample(data, min(5, len(data)))
            
            for char in selected:
                with st.expander(f"{char['fullName']}"):
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        st.image(char['imageUrl'], width=150)
                    with col2:
                        st.write(f"**Title:** {char.get('title', 'Unknown')}")
                        st.write(f"**Family:** {char.get('family', 'Unknown')}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
'''
    with open('pages/713_🌐_ThronesApi.py', 'w') as f:
        f.write(code)

if __name__ == "__main__":
    fix_placekeanu()
    fix_biriyani()
    fix_vadivelu()
    fix_harry_potter()
    fix_thrones()
    print("Fixed 5 image pages.")
