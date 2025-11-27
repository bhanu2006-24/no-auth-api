import os

def customize_pages():
    pages_dir = 'pages'
    
    # Define the content for each page
    pages_content = {
        "81_🌐_Cat_Facts_81.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Cat Facts", page_icon="🐱")

st.markdown("# 🐱 Daily Cat Facts")
st.sidebar.header("Cat Facts")
st.write("Get a random interesting fact about cats!")

if st.button("🐱 Get New Fact"):
    try:
        response = requests.get("https://cat-fact.herokuapp.com/facts/random?amount=1")
        if response.status_code == 200:
            data = response.json()
            fact = data.get("text", "No fact found.")
            st.info(f"**Did you know?** {fact}")
        else:
            st.error("Could not fetch cat fact.")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "82_🌐_Dog_Facts.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Dog Facts", page_icon="🐶")

st.markdown("# 🐶 Dog Facts")
st.sidebar.header("Dog Facts")
st.write("Learn something new about dogs!")

if st.button("🐶 Tell me about dogs"):
    try:
        response = requests.get("http://dog-api.kinduff.com/api/facts")
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                fact = data["facts"][0]
                st.success(f"**Woof!** {fact}")
            else:
                st.warning("No facts available right now.")
        else:
            st.error("API Error.")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "83_🌐_Dog_Facts_83.py": '''import streamlit as st
import requests

st.set_page_config(page_title="More Dog Facts", page_icon="🐕")

st.markdown("# 🐕 More Dog Facts")
st.sidebar.header("More Dog Facts")
st.write("Another source for dog wisdom.")

if st.button("🐕 Fetch Fact"):
    try:
        # Using the same API but styling differently as it was a duplicate in the list
        response = requests.get("http://dog-api.kinduff.com/api/facts")
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                fact = data["facts"][0]
                st.markdown(f"> *{fact}*")
            else:
                st.warning("No facts available.")
        else:
            st.error("API Error.")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "84_🌐_Dogs.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Dog Images", page_icon="🐩")

st.markdown("# 🐩 Random Dog Images")
st.sidebar.header("Dog Images")

if st.button("🐩 Show me a Dog"):
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        if response.status_code == 200:
            data = response.json()
            st.image(data["message"], caption="Good Boy!", use_column_width=True)
        else:
            st.error("API Error.")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "85_🌐_FishWatch.py": '''import streamlit as st
import requests

st.set_page_config(page_title="FishWatch", page_icon="🐟")

st.markdown("# 🐟 FishWatch Species")
st.sidebar.header("FishWatch")
st.write("Search for fish species data from NOAA.")

species = st.text_input("Enter Species Name (e.g., Red Snapper)", "Red Snapper")

if st.button("🔍 Search"):
    try:
        url = f"https://www.fishwatch.gov/api/species/{species}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                # API returns a list of dicts
                for fish in data:
                    st.subheader(fish.get("Species Name", "Unknown"))
                    
                    # Image
                    img_gallery = fish.get("Image Gallery")
                    if img_gallery:
                        if isinstance(img_gallery, list) and len(img_gallery) > 0:
                             st.image(img_gallery[0].get("src"), caption=img_gallery[0].get("alt"))
                        elif isinstance(img_gallery, dict):
                             st.image(img_gallery.get("src"), caption=img_gallery.get("alt"))

                    st.write(f"**Scientific Name:** {fish.get('Scientific Name')}")
                    st.write(f"**Habitat:** {fish.get('Habitat')}")
                    st.write(f"**Location:** {fish.get('Location')}")
                    
                    with st.expander("More Details"):
                        st.markdown(fish.get("Physical Description", ""))
                        st.markdown(f"**Population:** {fish.get('Population')}")
            else:
                st.warning("No fish found with that name.")
        else:
            st.error("API Error.")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "86_🌐_HTTP_Cat.py": '''import streamlit as st

st.set_page_config(page_title="HTTP Cat", page_icon="🐱")

st.markdown("# 🐱 HTTP Cat")
st.sidebar.header("HTTP Cat")
st.write("Visualizing HTTP Status Codes with Cats.")

code = st.number_input("Enter HTTP Status Code", min_value=100, max_value=599, value=200)

if code:
    url = f"https://http.cat/{code}"
    st.image(url, caption=f"Status Code: {code}")
''',

        "87_🌐_HTTP_Dog_87.py": '''import streamlit as st

st.set_page_config(page_title="HTTP Dog", page_icon="🐶")

st.markdown("# 🐶 HTTP Dog")
st.sidebar.header("HTTP Dog")
st.write("Visualizing HTTP Status Codes with Dogs.")

code = st.number_input("Enter HTTP Status Code", min_value=100, max_value=599, value=404)

if code:
    url = f"https://http.dog/{code}.jpg"
    st.image(url, caption=f"Status Code: {code}")
''',

        "88_🌐_MeowFacts.py": '''import streamlit as st
import requests

st.set_page_config(page_title="MeowFacts", page_icon="🐈")

st.markdown("# 🐈 MeowFacts")
st.write("Random facts about cats.")

if st.button("🐈 Get Fact"):
    try:
        response = requests.get("https://meowfacts.herokuapp.com/")
        if response.status_code == 200:
            data = response.json()
            st.success(data["data"][0])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "89_🌐_Movebank.py": '''import streamlit as st

st.set_page_config(page_title="Movebank", page_icon="🦅")

st.markdown("# 🦅 Movebank Animal Tracking")
st.write("""
Movebank is a free, online database of animal tracking data hosted by the Max Planck Institute of Animal Behavior.
Accessing the data often requires specific study IDs and permissions.
""")

st.info("Please visit the official Movebank website to explore the data map.")
st.markdown("[Go to Movebank.org](https://www.movebank.org/)")
''',

        "90_🌐_PlaceBear.py": '''import streamlit as st

st.set_page_config(page_title="PlaceBear", page_icon="🐻")

st.markdown("# 🐻 PlaceBear")
st.write("Generate placeholder bear images.")

col1, col2 = st.columns(2)
with col1:
    width = st.slider("Width", 100, 1000, 400)
with col2:
    height = st.slider("Height", 100, 1000, 300)

grayscale = st.checkbox("Grayscale")

if st.button("Generate Bear"):
    url = f"https://placebear.com/{'g/' if grayscale else ''}{width}/{height}"
    st.image(url, caption=f"Bear {width}x{height}")
    st.code(url)
''',

        "91_🌐_PlaceDog.py": '''import streamlit as st

st.set_page_config(page_title="PlaceDog", page_icon="🐩")

st.markdown("# 🐩 PlaceDog")
st.write("Generate placeholder dog images.")

col1, col2 = st.columns(2)
with col1:
    width = st.slider("Width", 100, 1000, 500)
with col2:
    height = st.slider("Height", 100, 1000, 400)

if st.button("Generate Dog"):
    url = f"https://placedog.net/{width}/{height}"
    st.image(url, caption=f"Dog {width}x{height}")
    st.code(url)
''',

        "92_🌐_RandomDog.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Random Dog", page_icon="🐕‍🦺")

st.markdown("# 🐕‍🦺 Random Dog")

if st.button("Fetch Dog"):
    try:
        response = requests.get("https://random.dog/woof.json")
        if response.status_code == 200:
            data = response.json()
            url = data["url"]
            if url.endswith(".mp4") or url.endswith(".webm"):
                st.video(url)
            else:
                st.image(url, use_column_width=True)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "93_🌐_RandomDuck.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Random Duck", page_icon="🦆")

st.markdown("# 🦆 Random Duck")

if st.button("Quack!"):
    try:
        response = requests.get("https://random-d.uk/api/v2/random")
        if response.status_code == 200:
            data = response.json()
            st.image(data["url"], caption=data.get("message", "Quack!"), use_column_width=True)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "94_🌐_RandomFox.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Random Fox", page_icon="🦊")

st.markdown("# 🦊 Random Fox")

if st.button("What does the fox say?"):
    try:
        response = requests.get("https://randomfox.ca/floof/")
        if response.status_code == 200:
            data = response.json()
            st.image(data["image"], use_column_width=True)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "95_🌐_RescueGroups.py": '''import streamlit as st

st.set_page_config(page_title="RescueGroups", page_icon="🐾")

st.markdown("# 🐾 RescueGroups.org")
st.write("Find adoptable pets.")

st.info("This API requires an API key for most operations. Please visit their website to search for pets.")
st.markdown("[RescueGroups.org](https://www.rescuegroups.org/)")
''',

        "96_🌐_ShibeOnline.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Shibe Online", page_icon="🐕")

st.markdown("# 🐕 Shibe Online")
st.write("Cute Shiba Inu pictures.")

count = st.slider("How many Shibes?", 1, 10, 1)

if st.button("Get Shibes"):
    try:
        response = requests.get(f"http://shibe.online/api/shibes?count={count}")
        if response.status_code == 200:
            urls = response.json()
            for url in urls:
                st.image(url, use_column_width=True)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "97_🌐_xenocanto.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Xeno-canto", page_icon="🐦")

st.markdown("# 🐦 Xeno-canto Bird Sounds")
st.write("Search for bird recordings from around the world.")

query = st.text_input("Search (e.g., 'cnt:brazil' or 'bearded bellbird')", "cnt:brazil")

if st.button("Search Recordings"):
    try:
        with st.spinner("Searching..."):
            response = requests.get(f"https://www.xeno-canto.org/api/2/recordings?query={query}")
            if response.status_code == 200:
                data = response.json()
                recordings = data.get("recordings", [])
                st.write(f"Found {len(recordings)} recordings.")
                
                for rec in recordings[:10]: # Limit to 10
                    st.markdown(f"### {rec['en']} ({rec['gen']} {rec['sp']})")
                    st.write(f"**Location:** {rec['cnt']}, {rec['loc']}")
                    st.audio(rec['file'])
                    st.markdown("---")
            else:
                st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "98_🌐_Zoo_Animals_98.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Zoo Animals", page_icon="🦁")

st.markdown("# 🦁 Zoo Animals")

if st.button("Get Random Animal"):
    try:
        response = requests.get("https://zoo-animal-api.herokuapp.com/animals/rand")
        if response.status_code == 200:
            data = response.json()
            st.header(data["name"])
            st.image(data["image_link"], caption=data["name"], use_column_width=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Latin Name:** {data['latin_name']}")
                st.write(f"**Animal Type:** {data['animal_type']}")
                st.write(f"**Active Time:** {data['active_time']}")
            with col2:
                st.write(f"**Lifespan:** {data['lifespan']} years")
                st.write(f"**Diet:** {data['diet']}")
                st.write(f"**Habitat:** {data['habitat']}")
                
            st.write(f"**Range:** {data['geo_range']}")
        else:
            st.error("API Error (The Zoo Animal API is often down/slow).")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "99_🌐_AnimeChan.py": '''import streamlit as st
import requests

st.set_page_config(page_title="AnimeChan", page_icon="👺")

st.markdown("# 👺 Anime Quotes")

if st.button("Get Random Quote"):
    try:
        response = requests.get("https://api.animechan.io/v1/quotes/random")
        if response.status_code == 200:
            data = response.json()
            st.markdown(f"### \"{data['data']['content']}\"")
            st.markdown(f"**— {data['data']['character']}** *({data['data']['anime']['name']})*")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "100_🌐_AnimeNewsNetwork.py": '''import streamlit as st

st.set_page_config(page_title="Anime News Network", page_icon="📰")

st.markdown("# 📰 Anime News Network")
st.write("The internet's most trusted anime news source.")

st.info("The ANN API returns XML which is complex to parse in this demo. Please visit their site for the latest news.")
st.markdown("[Visit AnimeNewsNetwork](https://www.animenewsnetwork.com/)")
'''
    }

    for filename, content in pages_content.items():
        filepath = os.path.join(pages_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Customized {filename}")

if __name__ == "__main__":
    customize_pages()
