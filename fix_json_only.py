import json
import re

with open('public/api/treatments.json', 'r') as f:
    data = json.load(f)

for item in data:
    if item.get('image'):
        old_path = item['image']
        match = re.match(r'assets/(.+?)-[A-Za-z0-9_-]+\.(jpg|jpeg|png)$', old_path)
        if match:
            base_name = match.group(1)
            ext = match.group(2)
            new_path = f"assets/{base_name}.{ext}"
            item['image'] = new_path

with open('public/api/treatments.json', 'w') as f:
    json.dump(data, f, indent=4)
