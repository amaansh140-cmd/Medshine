import os
import re
import shutil

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Change tailwind config colors
        content = content.replace("cream: '#ffffff'", "cream: '#FDFBF7'")
        content = content.replace("creamdeep: '#fafafa'", "creamdeep: '#F5F2EA'")
        
        # Change inline styles
        content = content.replace("background-color: #1a1a1a", "background-color: #065F46")
        content = content.replace("color: #1a1a1a", "color: #065F46")
        
        content = content.replace("background-color: #ffffff", "background-color: #FDFBF7")
        content = content.replace("color: #ffffff", "color: #FDFBF7")

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        shutil.copy(filename, f'../Medshine/{filename}')

