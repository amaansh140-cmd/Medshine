import os

# 1. Rename the file
old_file = 'treatment-skin-skin-whitening.html'
new_file = 'treatment-skin-skin-brightening.html'

if os.path.exists(old_file):
    os.rename(old_file, new_file)

# 2. Update contents of the new file
if os.path.exists(new_file):
    with open(new_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Case-sensitive replacements
    content = content.replace('Skin Whitening', 'Skin Brightening')
    content = content.replace('skin whitening', 'skin brightening')
    
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Update the link and text in treatment-skin.html
skin_file = 'treatment-skin.html'
if os.path.exists(skin_file):
    with open(skin_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('treatment-skin-skin-whitening.html', 'treatment-skin-skin-brightening.html')
    content = content.replace('Skin Whitening', 'Skin Brightening')
    
    with open(skin_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Renaming and text replacement complete.")
