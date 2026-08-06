import os
import glob
import re

files = glob.glob('*.html')
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Track if changes were made
    original_content = content
    
    # 1. blog.html
    content = content.replace("cosmetology Journals", "Clinical Cosmetology & Aesthetic Services")
    content = content.replace("cosmetology insights", "clinical cosmetology and aesthetic services insights")
    
    # 2. team.html
    content = content.replace("advanced cosmetological artistry.", "advanced clinical cosmetology and aesthetic services.")
    
    # 3. index.html & dr-priya.html
    content = content.replace("advancing cosmetological medicine.", "advancing clinical cosmetology and aesthetic services.")
    content = content.replace("complex cosmetological cases", "complex clinical cosmetology and aesthetic services cases")
    
    # 4. treatments.html
    content = content.replace("medical, cosmetological, and aesthetic treatments", "medical, clinical cosmetology, and aesthetic services")
    
    if content != original_content:
        with open(f, 'w') as file:
            file.write(content)
        print(f"Updated {f}")

