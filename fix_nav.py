import os
import shutil
import re

target_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Remove the About link which had href="dr-ankur.html" or similar
        content = re.sub(r'<a[^>]*>\s*About\s*</a>\s*', '', content)

        # 2. Remove transition.js script tag to restore native, robust navigation
        content = re.sub(r'<script src="(?:./)?(?:/)?src/transition\.js" type="module"></script>\s*', '', content)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

        if os.path.exists(f'../Medshine/{filename}'):
            shutil.copy(filename, f'../Medshine/{filename}')

# Also delete transition.js so it's fully gone
if os.path.exists('src/transition.js'):
    os.remove('src/transition.js')
if os.path.exists('../Medshine/src/transition.js'):
    os.remove('../Medshine/src/transition.js')

print("Navigation fixed and About menu removed!")
