import re
import glob

files = glob.glob('*.php')

for file in files:
    with open(file, 'r') as f:
        content = f.read()
        
    # Replace category links
    content = re.sub(r'href="treatment-([a-z-]+)\.html"', r'href="treatment_category.php?cat=\1"', content)
    
    with open(file, 'w') as f:
        f.write(content)

print("Links updated")
