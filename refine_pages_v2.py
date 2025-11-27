import os
import re

def refine_pages_v2():
    pages_dir = 'pages'
    
    # Smart Display Function Code
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

    files = os.listdir(pages_dir)
    count = 0
    
    for f in files:
        if not f.endswith('.py'):
            continue
            
        # Check number
        try:
            num = int(f.split('_')[0])
            if num <= 80:
                continue
        except:
            continue
            
        filepath = os.path.join(pages_dir, f)
        
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Extract Info using Regex
        # st.title("🌐 {api_name}")
        name_match = re.search(r'st\.title\("🌐 (.*?)"\)', content)
        # **URL:** [{api_url}]({api_url})
        url_match = re.search(r'\*\*URL:\*\* \[(.*?)\]', content)
        # Description is between st.markdown(""" and **URL
        desc_match = re.search(r'st\.markdown\("""(.*?)^\*\*URL', content, re.DOTALL | re.MULTILINE)
        
        if name_match and url_match:
            api_name = name_match.group(1)
            api_url = url_match.group(1)
            api_desc = desc_match.group(1).strip() if desc_match else ""
            
            # Reconstruct content
            new_content = f'''import streamlit as st
import requests

st.set_page_config(page_title="{api_name}", page_icon="🌐")

st.title("🌐 {api_name}")
st.markdown("""
{api_desc}

**URL:** [{api_url}]({api_url})
""")

# Smart Display Logic
{smart_display_code}

st.subheader("Live Demo")
url = st.text_input("API Endpoint", "{api_url}")

if st.button("Fetch Data"):
    try:
        with st.spinner("Fetching data..."):
            response = requests.get(url, timeout=5)
        
        st.write(f"**Status:** {{response.status_code}}")
        
        if response.status_code == 200:
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
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            
            count += 1
            if count % 50 == 0:
                print(f"Refined {count} pages...")
                
    print(f"Total refined: {count}")

if __name__ == "__main__":
    refine_pages_v2()
