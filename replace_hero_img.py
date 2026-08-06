import os

files = ['index.html', 'dr-priya.html']
old_str = 'public/headshot-3.jpg'
new_str = '/src/assets/dr_priya_portrait_pink.jpg'

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_str in content:
            content = content.replace(old_str, new_str)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filepath}")

