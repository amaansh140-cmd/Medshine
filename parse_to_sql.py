import os
import glob
from bs4 import BeautifulSoup

files = glob.glob('treatment-*.html')
inserts = []

for file in files:
    filename = file.replace('.html', '')
    parts = filename.split('-')
    
    if len(parts) == 2:
        # Category page (treatment-hair)
        continue
        
    # It's an individual treatment (treatment-hair-prp)
    category = parts[1]
    slug = '-'.join(parts[2:])
    
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    title_tag = soup.find('h1')
    title = title_tag.get_text(strip=True).replace("'", "\\'") if title_tag else 'Treatment'
    
    # Description
    desc = ''
    if title_tag:
        next_p = title_tag.find_next_sibling('p')
        if next_p:
            desc = next_p.get_text(strip=True).replace("'", "\\'")
            
    # Image
    imgs = soup.find_all('img')
    img_src = ''
    for img in imgs:
        if 'w-full' in img.get('class', []):
            img_src = img.get('src', '').replace('/src/', '')
            break
            
    if not img_src and imgs:
        img_src = imgs[0].get('src', '').replace('/src/', '')
        
    # Fix the .jpg hash issue: we don't know the exact hash here, but the user is uploading the new zip.
    # Wait, the images are already physically in `assets/`. We can just store the original name without hash,
    # OR we can glob the assets folder to find the hashed filename!
    if img_src.startswith('assets/'):
        base_name = img_src.split('/')[-1].split('.')[0] # treatment_hair_prp
        # try to find the hashed version
        matches = glob.glob(f'dist/assets/{base_name}*.jpg') + glob.glob(f'dist/assets/{base_name}*.jpeg') + glob.glob(f'dist/assets/{base_name}*.png')
        if matches:
            img_src = matches[0].replace('dist/', '')
            
    inserts.append(f"('{category}', '{slug}', '{title}', '{desc}', '{img_src}')")

print(f"Parsed {len(inserts)} treatments.")
with open('treatment_seeds.txt', 'w') as f:
    f.write(",\n".join(inserts))
