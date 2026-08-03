import glob
import re

for filename in glob.glob("*.html"):
    with open(filename, 'r') as f:
        content = f.read()
    
    if 'href="https://wa.me/"' in content:
        new_content = content.replace('href="https://wa.me/"', 'href="https://wa.me/917506251933"')
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Updated {filename}")
