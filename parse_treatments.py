import os
import glob
from bs4 import BeautifulSoup
import json
import re

files = glob.glob('treatment-*.html')
data = []

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    slug = file.replace('.html', '')
    title_tag = soup.find('h1')
    title = title_tag.get_text(strip=True) if title_tag else soup.title.string.split('|')[0].strip() if soup.title else 'Treatment'
    
    # Try to find the main description paragraph
    desc = ''
    if title_tag:
        # get next sibling p
        next_p = title_tag.find_next_sibling('p')
        if next_p:
            desc = next_p.get_text(strip=True)
            
    # Try to find an image (usually the first img that isn't an icon)
    # The structure has a big section. Let's look for img inside a div with border-radius maybe?
    imgs = soup.find_all('img')
    img_src = ''
    for img in imgs:
        if 'w-full' in img.get('class', []):
            img_src = img.get('src')
            break
            
    if not img_src and imgs:
        img_src = imgs[0].get('src')

    # Get the rest of the text content below the title
    # We can just extract everything inside the main container after the title
    content_html = ""
    if title_tag:
        parent = title_tag.parent
        # extract all elements after the description
        for sib in next_p.next_siblings if next_p else title_tag.next_siblings:
            if sib.name: # if it's an actual tag
                # remove any class attributes to make it cleaner or keep them?
                # We can keep them so it looks nice
                content_html += str(sib)

    data.append({
        'slug': slug,
        'title': title,
        'description': desc,
        'image': img_src,
        'content': content_html
    })

print(f"Parsed {len(data)} files.")
with open('treatments_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)
