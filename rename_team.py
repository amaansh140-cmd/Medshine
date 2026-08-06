import os
import re
import shutil

# First, rename the file locally
if os.path.exists('about.html'):
    shutil.move('about.html', 'team.html')
if os.path.exists('../Medshine/about.html'):
    os.remove('../Medshine/about.html')

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Remove grayscale
        content = re.sub(r'\bgrayscale\b', '', content)
        
        # 2. Update navigation hrefs
        content = content.replace('href="about.html"', 'href="team.html"')
        
        # 3. Update navigation text
        content = content.replace('>About Us<', '>Team<')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        shutil.copy(filename, f'../Medshine/{filename}')

