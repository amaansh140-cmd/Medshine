import os
import glob
import re

files = glob.glob('*.html')
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    new_content = re.sub(
        r'class="(absolute bottom-4 left-4 right-4 bg-[^"]*)"',
        r'class="\1 animate-float"',
        content
    )
    
    if new_content != content:
        with open(f, 'w') as file:
            file.write(new_content)
        print(f"Updated {f}")
