import os

def customize_pages():
    pages_dir = 'pages'
    
    pages_content = {
        "101_🌐_Catboy.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Catboy", page_icon="😸")

st.markdown("# 😸 Catboy Images")
st.sidebar.header("Catboy")
st.write("Random images of Catboys.")

if st.button("Get Catboy"):
    try:
        response = requests.get("https://api.catboys.com/img")
        if response.status_code == 200:
            data = response.json()
            st.image(data["url"], caption=f"Artist: {data.get('artist', 'Unknown')}", use_column_width=True)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "102_🌐_NekosBest.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Nekos.best", page_icon="😻")

st.markdown("# 😻 Nekos.best")
st.sidebar.header("Nekos.best")
st.write("Best Neko images and GIFs.")

category = st.selectbox("Category", ["neko", "kitsune", "husbando", "waifu"])

if st.button("Get Image"):
    try:
        response = requests.get(f"https://nekos.best/api/v2/{category}")
        if response.status_code == 200:
            data = response.json()
            result = data["results"][0]
            st.image(result["url"], caption=f"Artist: {result['artist_name']}", use_column_width=True)
            st.markdown(f"[Source]({result['source_url']})")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "103_🌐_Studio_Ghibli_103.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Studio Ghibli", page_icon="🎬")

st.markdown("# 🎬 Studio Ghibli Films")
st.sidebar.header("Studio Ghibli")
st.write("Explore the films of Studio Ghibli.")

if st.button("Load Films"):
    try:
        response = requests.get("https://ghibliapi.vercel.app/films")
        if response.status_code == 200:
            films = response.json()
            for film in films:
                with st.expander(f"{film['title']} ({film['release_date']})"):
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        st.image(film['image'], use_column_width=True)
                    with col2:
                        st.write(f"**Original Title:** {film['original_title']}")
                        st.write(f"**Director:** {film['director']}")
                        st.write(f"**Producer:** {film['producer']}")
                        st.write(f"**Running Time:** {film['running_time']} min")
                        st.write(f"**Rotten Tomatoes:** {film['rt_score']}%")
                        st.write(f"**Description:** {film['description']}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "104_🌐_Trace_Moe.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Trace.moe", page_icon="🔍")

st.markdown("# 🔍 Trace.moe")
st.write("Search for anime by screenshot.")

image_url = st.text_input("Enter Image URL", "https://images.plurk.com/32B15UXxymfSMwKGTObY5e.jpg")

if st.button("Trace Anime"):
    try:
        with st.spinner("Tracing..."):
            response = requests.get(f"https://api.trace.moe/search?url={image_url}")
            if response.status_code == 200:
                data = response.json()
                if data["result"]:
                    top_match = data["result"][0]
                    st.success(f"Found: {top_match['filename']}")
                    st.write(f"**Episode:** {top_match['episode']}")
                    st.write(f"**Similarity:** {top_match['similarity']:.2%}")
                    st.video(top_match['video'])
                    st.image(top_match['image'], caption="Scene Snapshot")
                else:
                    st.warning("No match found.")
            else:
                st.error(f"API Error: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "105_🌐_Waifuim.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Waifu.im", page_icon="💃")

st.markdown("# 💃 Waifu.im")
st.write("Search for Waifu images.")

is_nsfw = st.checkbox("NSFW (Enable at your own risk)", value=False)
tag = st.selectbox("Tag", ["maid", "waifu", "marin-kitagawa", "mori-calliope", "raiden-shogun", "oppai", "selfies", "uniform"])

if st.button("Get Waifu"):
    try:
        params = {"is_nsfw": str(is_nsfw).lower(), "included_tags": tag}
        response = requests.get("https://api.waifu.im/search", params=params)
        if response.status_code == 200:
            data = response.json()
            if data["images"]:
                img = data["images"][0]
                st.image(img["url"], caption=f"Tag: {tag}", use_column_width=True)
                st.markdown(f"[Source]({img['source']})")
            else:
                st.warning("No images found.")
        else:
            st.error(f"API Error: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "106_🌐_Waifupics.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Waifu.pics", page_icon="🖼️")

st.markdown("# 🖼️ Waifu.pics")
st.write("More Waifu pictures.")

category = st.selectbox("Category", ["waifu", "neko", "shinobu", "megumin", "bully", "cuddle", "cry", "hug", "awoo", "kiss", "lick", "pat", "smug", "bonk", "yeet", "blush", "smile", "wave", "highfive", "handhold", "nom", "bite", "glomp", "slap", "kill", "kick", "happy", "wink", "poke", "dance", "cringe"])

if st.button("Get Picture"):
    try:
        response = requests.get(f"https://api.waifu.pics/sfw/{category}")
        if response.status_code == 200:
            data = response.json()
            st.image(data["url"], caption=f"Category: {category}", use_column_width=True)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "107_🌐_URLhaus.py": '''import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="URLhaus", page_icon="🛡️")

st.markdown("# 🛡️ URLhaus Recent Malware URLs")
st.write("Recent malware URLs identified by URLhaus.")

if st.button("Fetch Recent URLs"):
    try:
        response = requests.get("https://urlhaus-api.abuse.ch/v1/urls/recent/")
        if response.status_code == 200:
            data = response.json()
            if data["query_status"] == "ok":
                urls = data["urls"]
                df = pd.DataFrame(urls)
                st.dataframe(df[["id", "url_status", "date_added", "url", "reporter", "threat", "tags"]])
            else:
                st.error("Query failed.")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "108_🌐_Art_Institute_of_Chicago.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Art Institute of Chicago", page_icon="🎨")

st.markdown("# 🎨 Art Institute of Chicago")
st.write("Explore the collection.")

if st.button("Get Random Artwork"):
    try:
        # Get a random page to simulate random artwork
        import random
        page = random.randint(1, 100)
        response = requests.get(f"https://api.artic.edu/api/v1/artworks?page={page}&limit=1")
        if response.status_code == 200:
            data = response.json()
            artwork = data["data"][0]
            st.header(artwork["title"])
            st.write(f"**Artist:** {artwork['artist_display']}")
            st.write(f"**Date:** {artwork['date_display']}")
            st.write(f"**Medium:** {artwork['medium_display']}")
            
            if artwork["image_id"]:
                img_url = f"https://www.artic.edu/iiif/2/{artwork['image_id']}/full/843,/0/default.jpg"
                st.image(img_url, caption=artwork["title"], use_column_width=True)
            else:
                st.warning("No image available for this artwork.")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "109_🌐_Colormind.py": '''import streamlit as st
import requests
import json

st.set_page_config(page_title="Colormind", page_icon="🌈")

st.markdown("# 🌈 Colormind Palette Generator")
st.write("Generate AI-powered color palettes.")

if st.button("Generate Palette"):
    try:
        response = requests.post("http://colormind.io/api/", data=json.dumps({"model": "default"}))
        if response.status_code == 200:
            data = response.json()
            palette = data["result"]
            
            cols = st.columns(5)
            for i, color in enumerate(palette):
                hex_color = '#{:02x}{:02x}{:02x}'.format(*color)
                with cols[i]:
                    st.color_picker(f"Color {i+1}", hex_color, disabled=True)
                    st.write(hex_color)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "110_🌐_ColourLovers.py": '''import streamlit as st
import requests

st.set_page_config(page_title="ColourLovers", page_icon="🎨")

st.markdown("# 🎨 ColourLovers Top Palettes")
st.write("Browse top palettes from ColourLovers.")

if st.button("Fetch Palettes"):
    try:
        # Note: ColourLovers API is HTTP
        response = requests.get("http://www.colourlovers.com/api/palettes/top?format=json", headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            palettes = response.json()
            for pal in palettes[:10]:
                st.subheader(pal["title"])
                st.write(f"By {pal['userName']}")
                st.image(pal["imageUrl"], use_column_width=True)
                st.markdown("---")
        else:
            st.error(f"API Error: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "111_🌐_Icon_Horse_111.py": '''import streamlit as st

st.set_page_config(page_title="Icon Horse", page_icon="🐴")

st.markdown("# 🐴 Icon Horse")
st.write("Get the favicon for any website.")

domain = st.text_input("Enter Domain (e.g., google.com)", "google.com")

if st.button("Get Icon"):
    url = f"https://icon.horse/icon/{domain}"
    st.image(url, caption=f"Icon for {domain}")
    st.code(url)
''',

        "112_🌐_Icons8.py": '''import streamlit as st

st.set_page_config(page_title="Icons8", page_icon="🎱")

st.markdown("# 🎱 Icons8")
st.write("Search for icons on Icons8.")

query = st.text_input("Search Icons", "home")

if st.button("Search"):
    st.markdown(f"**[Click here to search '{query}' on Icons8](https://icons8.com/icons/set/{query})**")
    st.info("Icons8 does not have a free public API for direct embedding without an API key, but you can browse their massive library via the link above.")
''',

        "113_🌐_Lordicon.py": '''import streamlit as st

st.set_page_config(page_title="Lordicon", page_icon="🔔")

st.markdown("# 🔔 Lordicon")
st.write("Animated icons library.")

st.info("Lordicon requires integration via their web components or specific embed codes. Visit their site to explore.")
st.markdown("[Visit Lordicon](https://lordicon.com/)")
''',

        "114_🌐_Metropolitan_Museum_of_Art.py": '''import streamlit as st
import requests
import random

st.set_page_config(page_title="The Met", page_icon="🏛️")

st.markdown("# 🏛️ The Metropolitan Museum of Art")
st.write("Explore the Met's collection.")

if st.button("Get Random Object"):
    try:
        # First get a list of object IDs (or just pick a random number range known to be valid, but searching is safer)
        # Let's search for "sunflowers" to get some IDs
        search_response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search?q=sunflowers&hasImages=true")
        if search_response.status_code == 200:
            ids = search_response.json()["objectIDs"]
            if ids:
                obj_id = random.choice(ids[:50]) # Pick from top 50
                
                obj_response = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}")
                if obj_response.status_code == 200:
                    obj = obj_response.json()
                    st.header(obj["title"])
                    st.write(f"**Artist:** {obj['artistDisplayName']}")
                    st.write(f"**Date:** {obj['objectDate']}")
                    st.write(f"**Medium:** {obj['medium']}")
                    st.image(obj["primaryImage"], use_column_width=True)
                else:
                    st.error("Failed to fetch object details.")
            else:
                st.warning("No objects found.")
        else:
            st.error("Search failed.")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "115_🌐_PHPNoise.py": '''import streamlit as st

st.set_page_config(page_title="PHP Noise", page_icon="🌫️")

st.markdown("# 🌫️ PHP Noise Generator")
st.write("Generate noise background images.")

r = st.slider("Red", 0, 255, 100)
g = st.slider("Green", 0, 255, 100)
b = st.slider("Blue", 0, 255, 100)
tiles = st.slider("Tiles", 1, 50, 10)

if st.button("Generate Noise"):
    url = f"http://php-noise.com/noise.php?r={r}&g={g}&b={b}&tiles={tiles}&json"
    # The API returns JSON with a base64 uri or just the image if no json param
    # Let's use direct image url
    img_url = f"http://php-noise.com/noise.php?r={r}&g={g}&b={b}&tiles={tiles}"
    st.image(img_url, caption="Generated Noise")
    st.code(img_url)
''',

        "116_🌐_Pixel_Encounter_116.py": '''import streamlit as st

st.set_page_config(page_title="Pixel Encounter", page_icon="👾")

st.markdown("# 👾 Pixel Encounter Monsters")
st.write("Generate random pixel monsters.")

width = st.slider("Width", 100, 500, 200)

if st.button("Generate Monster"):
    # Using a random ID to force refresh
    import random
    rand_id = random.randint(1, 10000)
    url = f"https://pixelencounter.com/api/basic/monsters/random/png?width={width}&_={rand_id}"
    st.image(url, caption="Pixel Monster")
''',

        "117_🌐_xColors.py": '''import streamlit as st
import requests

st.set_page_config(page_title="xColors", page_icon="🎨")

st.markdown("# 🎨 xColors Random Color")
st.write("Get a random color.")

if st.button("Get Color"):
    try:
        response = requests.get("https://x-colors.yurace.pro/api/random")
        if response.status_code == 200:
            data = response.json()
            hex_code = data["hex"]
            rgb = data["rgb"]
            
            st.color_picker("Color", hex_code, disabled=True)
            st.write(f"**HEX:** {hex_code}")
            st.write(f"**RGB:** {rgb}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "118_🌐_Chainlink.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Chainlink", page_icon="🔗")

st.markdown("# 🔗 Chainlink Price Feeds")
st.write("Latest price data from Chainlink.")

st.info("Direct access to Chainlink data usually requires a Web3 provider or specific contract calls. This is a placeholder for the concept.")
st.markdown("[Explore Chainlink Data Feeds](https://data.chain.link/)")
''',

        "119_🌐_Chainpoint.py": '''import streamlit as st

st.set_page_config(page_title="Chainpoint", page_icon="⛓️")

st.markdown("# ⛓️ Chainpoint")
st.write("Anchor data to the Bitcoin blockchain.")

st.info("Chainpoint allows you to prove data integrity. Visit their site for documentation and tools.")
st.markdown("[Chainpoint.org](https://chainpoint.org/)")
''',

        "120_🌐_Helium.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Helium", page_icon="🎈")

st.markdown("# 🎈 Helium Network Stats")
st.write("Stats from the Helium blockchain.")

if st.button("Get Stats"):
    try:
        response = requests.get("https://api.helium.io/v1/stats")
        if response.status_code == 200:
            data = response.json()["data"]
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Hotspots", data["counts"]["hotspots"])
                st.metric("Total Blocks", data["counts"]["blocks"])
            with col2:
                st.metric("Challenges", data["counts"]["challenges"])
                st.metric("Consensus Groups", data["counts"]["consensus_groups"])
                
            st.json(data)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
'''
    }

    for filename, content in pages_content.items():
        filepath = os.path.join(pages_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Customized {filename}")

if __name__ == "__main__":
    customize_pages()
