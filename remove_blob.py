import os
import re
import shutil

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Update Tailwind config colors (ink -> deep emerald, inkmute -> lighter emerald)
        # We look for ink: '#1a1a1a' or similar.
        content = re.sub(r"ink:\s*'#[0-9a-fA-F]+'", "ink: '#065F46'", content)
        content = re.sub(r"inkmute:\s*'#[0-9a-fA-F]+'", "inkmute: '#059669'", content)

        # 2. Remove SVG mask block
        content = re.sub(r'<svg class="svg-defs">.*?</svg>\s*', '', content, flags=re.DOTALL)

        # 3. Handle index.html structure
        if filename == 'index.html':
            # Remove <div class="hero">
            content = content.replace('<div class="hero">', '')
            
            # Remove <!-- Base Layer --> and <div class="layer base-layer">
            content = content.replace('<!-- Base Layer -->', '')
            content = content.replace('<div class="layer base-layer">', '')
            
            # Remove reveal layer
            parts = re.split(r'<!-- Reveal Layer -->', content, flags=re.IGNORECASE)
            if len(parts) > 1:
                part0 = parts[0]
                part1 = parts[1]
                
                # part0 needs its last </div> removed (which closed base-layer)
                last_div_idx = part0.rfind('</div>')
                if last_div_idx != -1:
                    part0 = part0[:last_div_idx] + part0[last_div_idx+6:]
                    
                # part1 needs everything up to <script type="module" removed, plus one </div> for hero
                script_idx = part1.find('<script type="module"')
                if script_idx != -1:
                    content = part0 + "\n    " + part1[script_idx:]
                else:
                    content = part0 + "\n"
        else:
            # Handle standard structure
            content = content.replace('<div class="scroll-page-wrapper">', '')
            content = content.replace('<!-- BASE LAYER -->', '')
            content = content.replace('<div class="scroll-base-layer layer base-layer">', '')
            
            # Remove reveal layer
            parts = re.split(r'<!-- REVEAL LAYER -->', content, flags=re.IGNORECASE)
            if len(parts) > 1:
                part0 = parts[0]
                part1 = parts[1]
                
                # part0 needs its last </div> removed (which closed base-layer)
                last_div_idx = part0.rfind('</div>')
                if last_div_idx != -1:
                    part0 = part0[:last_div_idx] + part0[last_div_idx+6:]
                    
                # part1 needs everything up to <script type="module" removed
                script_idx = part1.find('<script type="module"')
                if script_idx != -1:
                    content = part0 + "\n    " + part1[script_idx:]
                else:
                    content = part0 + "\n"
                    
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        shutil.copy(filename, f'../Medshine/{filename}')

