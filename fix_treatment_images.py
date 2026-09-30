import json
import re
import os
import shutil

# 1. Update treatments.json
with open('public/api/treatments.json', 'r') as f:
    data = json.load(f)

for item in data:
    if item.get('image'):
        old_path = item['image']
        # e.g. "assets/treatment_face_prp_indian-Cz1DsPl6.jpeg"
        # Extract the base name without the hash
        match = re.match(r'assets/(.+?)-[A-Za-z0-9_-]+\.(jpg|jpeg|png)$', old_path)
        if match:
            base_name = match.group(1)
            ext = match.group(2)
            new_path = f"{base_name}.{ext}"
            item['image'] = new_path
            
            # 2. Copy the file from src/assets to public/
            src_file = f"src/assets/{new_path}"
            dest_file = f"public/{new_path}"
            
            if os.path.exists(src_file):
                shutil.copy(src_file, dest_file)
            else:
                print(f"Warning: {src_file} not found!")
        else:
            # Maybe already fixed or different format
            pass

with open('public/api/treatments.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Fixed treatments.json and copied images to public/!")
