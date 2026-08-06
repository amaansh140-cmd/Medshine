import re
import shutil

files = ['index.html', 'about.html', 'contact.html', 'dr-ankur.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The reveal layer is named <!-- ================= REVEAL LAYER (DARK MODE) ================= -->
    parts = re.split(r'<!-- ================= REVEAL LAYER \(DARK MODE\) ================= -->', content, flags=re.IGNORECASE)
    
    if len(parts) > 1:
        part0 = parts[0]
        part1 = parts[1]
        
        # In part0, remove the LAST </div> (which closed base-layer)
        # Note that index.html might have </div> <!-- End Base Layer -->
        # We can just look for the last </div> and remove it, and any optional comment.
        last_div_match = list(re.finditer(r'</div>(?:\s*<!--[^>]*-->)?\s*$', part0))
        if last_div_match:
            part0 = part0[:last_div_match[-1].start()]
        else:
            # Fallback if the regex above didn't catch it
            last_div_idx = part0.rfind('</div>')
            if last_div_idx != -1:
                # find the end of the line
                end_of_line = part0.find('\n', last_div_idx)
                if end_of_line == -1: end_of_line = len(part0)
                part0 = part0[:last_div_idx] + part0[end_of_line:]

        # In part1, skip until <script type="module"
        script_idx = part1.find('<script type="module"')
        if script_idx != -1:
            content = part0 + "\n\n    " + part1[script_idx:]
        else:
            content = part0 + "\n"
            
    # Also strip the <svg class="svg-defs"> if any is left over
    content = re.sub(r'<svg class="svg-defs".*?</svg>\s*', '', content, flags=re.DOTALL)
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    shutil.copy(filename, f'../Medshine/{filename}')

