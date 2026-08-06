import os
import shutil
from bs4 import BeautifulSoup
import re

target_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        
        # 1. Headers: h1, h2 -> reveal-fade
        for tag in soup.find_all(['h1', 'h2']):
            classes = tag.get('class', [])
            if 'reveal-fade' not in classes:
                classes.append('reveal-fade')
                tag['class'] = classes

        # 2. Grids -> stagger-group
        for tag in soup.find_all('div', class_=re.compile(r'\bgrid\b')):
            classes = tag.get('class', [])
            if 'stagger-group' not in classes:
                classes.append('stagger-group')
                tag['class'] = classes
            
            # Direct children of grid -> reveal-anim
            for child in tag.find_all(recursive=False):
                if child.name in ['div', 'a', 'article']:
                    child_classes = child.get('class', [])
                    if 'reveal-anim' not in child_classes and 'reveal-fade' not in child_classes:
                        child_classes.append('reveal-anim')
                        child['class'] = child_classes

        # 3. Interactive elements -> hover-scale
        # Buttons and cards
        for tag in soup.find_all(['a', 'button']):
            classes = tag.get('class', [])
            # If it's a pill button (rounded-full) or a card (group)
            is_pill = any('rounded-full' in c for c in classes)
            is_card = 'group' in classes
            if (is_pill or is_card) and 'hover-scale' not in classes:
                classes.append('hover-scale')
                tag['class'] = classes

        # 4. Standalone images -> reveal-fade
        for tag in soup.find_all('img'):
            # Skip images inside the slider to avoid messing up the slider
            parent_classes = tag.parent.get('class', []) if tag.parent else []
            if not any('slider' in c for c in parent_classes) and not tag.find_parent(id=re.compile('slider')):
                classes = tag.get('class', [])
                if 'reveal-fade' not in classes and 'reveal-anim' not in classes:
                    classes.append('reveal-fade')
                    tag['class'] = classes

        new_content = str(soup)
        
        # Un-escape script tags that might get messed up by bs4 if not careful
        # Usually bs4 handles HTML5 fine.
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        if os.path.exists(f'../Medshine/{filename}'):
            shutil.copy(filename, f'../Medshine/{filename}')

print("Animations applied to all HTML files!")
