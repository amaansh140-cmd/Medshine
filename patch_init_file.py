import json

with open('treatments_data.json', 'r') as f:
    data = json.load(f)

formatted = []
for t in data:
    if '-' not in t['slug'].replace('treatment-', ''):
        continue
        
    parts = t['slug'].replace('treatment-', '').split('-')
    cat = parts[0]
    slug = '-'.join(parts[1:])
    img = t['image'].replace('/src/', '')
    if img.startswith('assets/'):
        import glob
        base = img.split('/')[-1].split('.')[0]
        matches = glob.glob(f'dist/assets/{base}*.jpg') + glob.glob(f'dist/assets/{base}*.jpeg') + glob.glob(f'dist/assets/{base}*.png')
        if matches:
            img = matches[0].replace('dist/', '')
            
    formatted.append({
        'category': cat,
        'slug': slug,
        'title': t['title'],
        'description': t['description'],
        'image': img
    })

# Write to a clean JSON file
with open('public/api/treatments.json', 'w') as f:
    json.dump(formatted, f)

# Patch init.php to read the file
with open('public/api/init.php', 'r') as f:
    content = f.read()

# We need to replace the long $json = '...'; line with file_get_contents
import re
content = re.sub(r'\$json = \'.*\';', '$json = file_get_contents(__DIR__ . "/treatments.json");', content)

with open('public/api/init.php', 'w') as f:
    f.write(content)
