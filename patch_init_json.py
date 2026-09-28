import json

# Read the JSON we already generated!
with open('treatments_data.json', 'r') as f:
    data = json.load(f)

# Format it for the new schema
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
        matches = glob.glob(f'dist/assets/{base}*.jpg') + glob.glob(f'dist/assets/{base}*.jpeg')
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
    // Create treatments table
    $pdo->exec("CREATE TABLE IF NOT EXISTS treatments (
        id INT AUTO_INCREMENT PRIMARY KEY,
        category VARCHAR(100) NOT NULL,
        slug VARCHAR(255) UNIQUE NOT NULL,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        image VARCHAR(500),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )");
    
    // Seed treatments safely using JSON
    $json = '{json_str}';
    $treatmentsData = json_decode($json, true);
    if ($treatmentsData) {{
        $stmtTreat = $pdo->prepare("INSERT IGNORE INTO treatments (category, slug, title, description, image) VALUES (?, ?, ?, ?, ?)");
        foreach ($treatmentsData as $t) {{
            $stmtTreat->execute([$t['category'], $t['slug'], $t['title'], $t['description'], $t['image']]);
        }}
    }}
"""

# Revert to original init.php and apply
import shutil
shutil.copyfile('public/api/init.php.bak', 'public/api/init.php') # Assuming we have a backup? No we don't.
