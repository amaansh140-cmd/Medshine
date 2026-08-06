import re
import shutil

files = ['about.html', 'contact.html', 'dr-priya.html', 'dr-ankur.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove SVG mask block
    content = re.sub(r'<svg class="svg-defs".*?</svg>\s*', '', content, flags=re.DOTALL)

    # Remove the wrappers
    content = content.replace('<div class="scroll-page-wrapper">', '')
    content = content.replace('<!-- ================= BASE LAYER (LIGHT) ================= -->', '')
    content = content.replace('<div class="scroll-base-layer layer base-layer">', '')
    
    # Remove reveal layer
    parts = re.split(r'<!-- ================= REVEAL LAYER \(DARK\) ================= -->', content, flags=re.IGNORECASE)
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

