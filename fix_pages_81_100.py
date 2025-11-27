import os
import streamlit as st

def fix_pages():
    pages_dir = 'pages'
    
    updates = {
        "81_🌐_Cat_Facts_81.py": "https://cat-fact.herokuapp.com/facts",
        "82_🌐_Dog_Facts.py": "http://dog-api.kinduff.com/api/facts",
        "83_🌐_Dog_Facts_83.py": "http://dog-api.kinduff.com/api/facts",
        "84_🌐_Dogs.py": "https://dog.ceo/api/breeds/image/random",
        "85_🌐_FishWatch.py": "https://www.fishwatch.gov/api/species",
        "86_🌐_HTTP_Cat.py": "https://http.cat/200",
        "87_🌐_HTTP_Dog_87.py": "https://http.dog/200.jpg",
        "88_🌐_MeowFacts.py": "https://meowfacts.herokuapp.com/",
        "89_🌐_Movebank.py": "https://www.movebank.org/movebank/service/direct-read", 
        "90_🌐_PlaceBear.py": "https://placebear.com/200/300",
        "91_🌐_PlaceDog.py": "https://placedog.net/500",
        "92_🌐_RandomDog.py": "https://random.dog/woof.json",
        "93_🌐_RandomDuck.py": "https://random-d.uk/api/v2/random",
        "94_🌐_RandomFox.py": "https://randomfox.ca/floof/",
        "95_🌐_RescueGroups.py": "https://api.rescuegroups.org/v5/public/animals/search/available/",
        "96_🌐_ShibeOnline.py": "http://shibe.online/api/shibes?count=1",
        "97_🌐_xenocanto.py": "https://www.xeno-canto.org/api/2/recordings?query=cnt:brazil",
        "98_🌐_Zoo_Animals_98.py": "https://zoo-animal-api.herokuapp.com/animals/rand",
        "99_🌐_AnimeChan.py": "https://api.animechan.io/v1/quotes/random",
        "100_🌐_AnimeNewsNetwork.py": "https://www.animenewsnetwork.com/encyclopedia/api.php?title=4658",
    }

    smart_display_code = """
def smart_display(data):
    # 1. Handle Lists
    if isinstance(data, list):
        if len(data) > 0 and isinstance(data[0], dict):
            st.dataframe(data)
            # Also check first item for image
            first_item = data[0]
            for k, v in first_item.items():
                if isinstance(v, str) and (v.endswith('.jpg') or v.endswith('.png') or v.endswith('.gif') or v.startswith('http')):
                    if 'image' in k.lower() or 'img' in k.lower() or 'url' in k.lower() or 'src' in k.lower():
                        st.image([item.get(k) for item in data[:5] if item.get(k)], width=200)
                        break
        else:
            st.write(data)
        return

    # 2. Handle Dictionaries
    if isinstance(data, dict):
        # Check for Images
        for k, v in data.items():
            if isinstance(v, str) and (v.endswith('.jpg') or v.endswith('.png') or v.endswith('.gif')):
                st.image(v, caption=k)
                return
            # Check for common image keys even if extension is missing (sometimes)
            if 'image' in k.lower() and isinstance(v, str) and v.startswith('http'):
                st.image(v, caption=k)
                return
        
        # Check for Quotes/Facts/Text
        for k, v in data.items():
            if k.lower() in ['quote', 'fact', 'joke', 'text', 'setup', 'delivery', 'advice']:
                st.info(f"**{k.capitalize()}:** {v}")
                # Don't return, might have more info
        
        # Check for nested data
        for k, v in data.items():
            if isinstance(v, (dict, list)):
                with st.expander(f"{k} Details"):
                    smart_display(v)
                    
        # Display simple key-values
        for k, v in data.items():
            if isinstance(v, (str, int, float, bool)) and k.lower() not in ['quote', 'fact', 'joke', 'text', 'setup', 'delivery', 'advice']:
                 # Filter out image urls we already showed
                 if isinstance(v, str) and v.startswith('http') and ('image' in k.lower() or 'img' in k.lower()):
                     continue
                 st.write(f"**{k}:** {v}")
"""

    for filename, new_url in updates.items():
        filepath = os.path.join(pages_dir, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filename}")
            continue
            
        # Read existing file to get Title and Description (if possible)
        # Or just use the filename to derive title
        
        # Simple parsing to preserve title
        with open(filepath, 'r') as f:
            content = f.read()
            
        # Extract title
        import re
        title_match = re.search(r'st\.title\("🌐 (.*?)"\)', content)
        api_name = title_match.group(1) if title_match else filename.split('_')[2].replace('.py', '')
        
        # Create new content
        new_content = f'''import streamlit as st
import requests

st.set_page_config(page_title="{api_name}", page_icon="🌐")

st.title("🌐 {api_name}")
st.markdown("""
Explore the {api_name} API.

**URL:** [{new_url}]({new_url})
""")

# Smart Display Logic
{smart_display_code}

st.subheader("Live Demo")
url = st.text_input("API Endpoint", "{new_url}")

if st.button("Fetch Data"):
    try:
        with st.spinner("Fetching data..."):
            response = requests.get(url, timeout=5)
        
        st.write(f"**Status:** {{response.status_code}}")
        
        if response.status_code == 200:
            # Check Content Type for Images
            content_type = response.headers.get('Content-Type', '')
            if 'image' in content_type:
                st.image(response.content, caption="Response Image")
            else:
                try:
                    data = response.json()
                    
                    # Use Smart Display
                    st.success("Data fetched successfully!")
                    smart_display(data)
                    
                    with st.expander("View Raw JSON"):
                        st.json(data)
                        
                except ValueError:
                    st.warning("Response is not JSON. Displaying as text:")
                    st.text(response.text[:1000])
        else:
            st.error("Failed to fetch data.")
            
    except Exception as e:
        st.error(f"An error occurred: {{e}}")
'''
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filename}")

if __name__ == "__main__":
    fix_pages()
