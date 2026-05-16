import os
import re

files_to_update = [
    "/Users/mac/Library/Mobile Documents/com~apple~CloudDocs/Desktop/projects/kim/modeles/pista-hr.html",
    "/Users/mac/Library/Mobile Documents/com~apple~CloudDocs/Desktop/projects/kim/modeles/pista-hr-plus.html"
]

def replace_ext(match):
    return re.sub(r'\.(jpg|jpeg|png|JPG|JPEG|PNG)$', '.webp', match.group(0))

for fpath in files_to_update:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(r'(?:\.\./)?media/pista-hr(?:-plus)?/[^"\'\s]+\.(?:jpg|jpeg|png|JPG|JPEG|PNG)', replace_ext, content)
    
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {fpath}")
