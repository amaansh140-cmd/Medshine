import re
import shutil

treatments = [
    "treatment-regenerative-prp.html",
    "treatment-regenerative-prf.html",
    "treatment-regenerative-exosome.html",
    "treatment-regenerative-regenera-activa.html",
    "treatment-regenerative-autologous-fat.html",
    "treatment-regenerative-stem-cell.html"
]

for file in treatments:
    with open(file, 'r') as f:
        content = f.read()
    
    # We want to remove any aspect-video div that contains "treatment_regen_" or doesn't contain the indian image
    # Actually, a simpler way is to find all aspect-video divs and only keep the first one in each section (base/reveal)
    
    parts = content.split("<!-- REVEAL LAYER -->")
    
    # Function to keep only the first image block in a layer
    def keep_first_image_block(html):
        # Find all image blocks
        blocks = re.findall(r'(<div class="aspect-video.*?</div>)', html, flags=re.DOTALL)
        if len(blocks) > 1:
            # We only want to keep the FIRST one. The others we replace with empty string
            for block in blocks[1:]:
                # Be careful to only replace the block itself, not all blocks
                html = html.replace(block, "", 1)
        return html

    parts[0] = keep_first_image_block(parts[0])
    if len(parts) > 1:
        parts[1] = keep_first_image_block(parts[1])
        
    content = "<!-- REVEAL LAYER -->".join(parts)
    
    with open(file, 'w') as f:
        f.write(content)
        
    shutil.copy(file, f'../Medshine/{file}')

