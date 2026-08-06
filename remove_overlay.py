import os
import shutil
import re

target_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove the overlay div
        new_content = re.sub(r'<div class="page-transition-overlay"></div>\s*', '', content)
        
        # Also let's remove it if it has an ID or other variations just in case
        new_content = re.sub(r'<div id="page-transition-overlay"[^>]*></div>\s*', '', new_content)

        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)

            if os.path.exists(f'../Medshine/{filename}'):
                shutil.copy(filename, f'../Medshine/{filename}')

print("Overlay removed from all files!")
