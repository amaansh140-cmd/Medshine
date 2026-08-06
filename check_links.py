import os
import glob
import re

html_files = glob.glob('*.html')
existing_files = set(html_files)
broken_links = []

for f in html_files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Find all hrefs
    hrefs = re.findall(r'href="([^"]+)"', content)
    for href in hrefs:
        # Ignore external links, anchors, and tel/mailto
        if href.startswith(('http', '#', 'tel:', 'mailto:', 'javascript:')):
            continue
        # Check if the file exists
        target = href.split('#')[0] # remove hash
        if target and target not in existing_files:
            broken_links.append((f, target))

if broken_links:
    print("Broken links found:")
    for src, target in broken_links:
        print(f"In {src}: {target}")
else:
    print("No broken internal links found.")
