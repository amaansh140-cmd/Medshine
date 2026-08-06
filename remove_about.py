import os
import shutil
import re

# 1. Remove about.html
if os.path.exists('about.html'):
    os.remove('about.html')
if os.path.exists('../Medshine/about.html'):
    os.remove('../Medshine/about.html')

# 2. Remove About from main.js (Mobile Drawer)
main_js_path = 'src/main.js'
if os.path.exists(main_js_path):
    with open(main_js_path, 'r', encoding='utf-8') as f:
        main_js = f.read()
    
    # Remove the mobile drawer link
    main_js = re.sub(r'<a href="about\.html" class="mobile-drawer-link">.*?</a>\s*', '', main_js)
    
    with open(main_js_path, 'w', encoding='utf-8') as f:
        f.write(main_js)
        
    shutil.copy(main_js_path, '../Medshine/' + main_js_path)

# 3. Remove About from all HTML files (Desktop Menu)
target_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Regex to match the About link in the nav
        # Typically looks like: <a class="hover:text-ink transition-colors" href="about.html">About</a>
        # Or with "About Us"
        new_content = re.sub(r'<a[^>]*href="about\.html"[^>]*>.*?</a>\s*', '', content)
        
        # Also remove Team if they had a Team link that they want removed? The user said "remove the about page".
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            if os.path.exists(f'../Medshine/{filename}'):
                shutil.copy(filename, f'../Medshine/{filename}')

print("About page and links removed!")
