import os
import glob
import re

files = glob.glob('*.html')
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Replace dermatology -> cosmetology (case sensitive preserve roughly)
    new_content = re.sub(r'\bdermatology\b', 'cosmetology', content, flags=re.IGNORECASE)
    # Fix casing for capitalized words
    new_content = re.sub(r'\bDermatology\b', 'Cosmetology', new_content)
    new_content = re.sub(r'\bDERMATOLOGY\b', 'COSMETOLOGY', new_content)

    new_content = re.sub(r'\bdermatological\b', 'cosmetological', new_content, flags=re.IGNORECASE)
    new_content = re.sub(r'\bDermatological\b', 'Cosmetological', new_content)
    new_content = re.sub(r'\bDERMATOLOGICAL\b', 'COSMETOLOGICAL', new_content)

    if content != new_content:
        with open(f, 'w') as file:
            file.write(new_content)
        print(f"Updated {f}")

