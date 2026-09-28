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

json_str = json.dumps(formatted).replace("'", "\\'")

php_code = f"""
    $json = '{json_str}';
    $treatmentsData = json_decode($json, true);
    if ($treatmentsData) {{
        $stmtTreat = $pdo->prepare("INSERT IGNORE INTO treatments (category, slug, title, description, image) VALUES (?, ?, ?, ?, ?)");
        foreach ($treatmentsData as $t) {{
            $stmtTreat->execute([$t['category'], $t['slug'], $t['title'], $t['description'], $t['image']]);
        }}
    }}
"""

with open('public/api/init.php', 'r') as f:
    content = f.read()

content = content.replace('// TREATMENTS_JSON_PLACEHOLDER', php_code)

with open('public/api/init.php', 'w') as f:
    f.write(content)
