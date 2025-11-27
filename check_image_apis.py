import os
import re

def check_image_apis():
    # 1. Parse apis.md for image keywords
    image_apis = []
    with open('apis.md', 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        if not line.strip().startswith('|'):
            continue
        parts = [p.strip() for p in line.split('|')]
        if len(parts) < 4:
            continue
            
        name_col = parts[1]
        desc_col = parts[2]
        
        # Check for keywords in description or name
        keywords = ['image', 'photo', 'picture', 'avatar', 'meme', 'gif', 'cat', 'dog', 'fox', 'bear']
        text = (name_col + " " + desc_col).lower()
        
        if any(k in text for k in keywords):
            match = re.search(r'\[(.*?)\]\((.*?)\)', name_col)
            if match:
                name = match.group(1)
                image_apis.append(name)

    print(f"Found {len(image_apis)} potential image APIs in apis.md")

    # 2. Check existing pages
    pages_dir = 'pages'
    files = [f for f in os.listdir(pages_dir) if f.endswith('.py')]
    
    suspicious = []
    
    for api_name in image_apis:
        # Find corresponding file
        # Normalize name
        norm_name = re.sub(r'[^a-zA-Z0-9]', '', api_name).lower()
        
        found_file = None
        for f in files:
            # Filename: 123_Emoji_Name.py
            parts = f.split('_')
            if len(parts) >= 3:
                file_name_norm = "".join(parts[2:]).replace('.py', '').lower()
                if norm_name in file_name_norm or file_name_norm in norm_name:
                    found_file = f
                    break
        
        if found_file:
            with open(os.path.join(pages_dir, found_file), 'r') as f:
                content = f.read()
                
            if 'st.image' not in content and 'st.video' not in content:
                suspicious.append({'api': api_name, 'file': found_file})
    
    print(f"Found {len(suspicious)} image APIs that might not be showing images:")
    for s in suspicious:
        print(f"{s['api']} -> {s['file']}")

if __name__ == "__main__":
    check_image_apis()
