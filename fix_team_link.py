import os
import shutil

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update navigation hrefs
        content = content.replace('href="team.html"', 'href="dr-ankur.html"')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        shutil.copy(filename, f'../Medshine/{filename}')

