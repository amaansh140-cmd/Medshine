import os
import shutil
from bs4 import BeautifulSoup

for filename in ['index.html', 'dr-priya.html', 'dr-ankur.html']:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    # Find spans with text "Areas of Clinical Focus" (case-insensitive in bs4 with lambda)
    spans = soup.find_all(lambda tag: tag.name == "span" and "Areas of Clinical Focus" in tag.text)
    
    modified = False
    for span in spans:
        # The parent header block we want to remove is a div with flex-col, etc.
        # It's usually the parent's parent. Let's find the closest parent div with 'mb-16' and 'gap-6'.
        header_div = span.find_parent('div', class_=lambda c: c and 'mb-16' in c and 'gap-6' in c)
        if header_div:
            header_div.decompose()
            modified = True
            
    if modified:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        if os.path.exists(f'../Medshine/{filename}'):
            shutil.copy(filename, f'../Medshine/{filename}')

print("Done removing 'Areas of Clinical Focus' headers.")
