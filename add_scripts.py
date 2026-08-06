import os
import shutil

target_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        if 'src="/src/animations.js"' not in content and 'src="src/animations.js"' not in content and 'src="./src/animations.js"' not in content:
            content = content.replace('</body>', '  <script src="src/animations.js" type="module"></script>\n</body>')
            changed = True

        if 'src="/src/transition.js"' not in content and 'src="src/transition.js"' not in content and 'src="./src/transition.js"' not in content:
            content = content.replace('</body>', '  <script src="src/transition.js" type="module"></script>\n</body>')
            changed = True

        if changed:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
                
            if os.path.exists(f'../Medshine/{filename}'):
                shutil.copy(filename, f'../Medshine/{filename}')

print("Scripts added!")
