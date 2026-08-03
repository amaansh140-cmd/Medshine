import re

filename = "treatment-injectables.html"

mappings = {
    "Scar subscision treatment": "treatment_injectables_scar_subcision.jpg",
    "Skin meso": "treatment_injectables_skin_meso.jpg",
    "Skin booster": "treatment_injectables_skin_booster.jpg"
}

with open(filename, 'r') as f:
    content = f.read()

# Split by the blocks that contain the title
blocks = re.split(r'(<a href="treatment-injectables-[a-z0-9-]+\.html")', content)

new_content = blocks[0]

for i in range(1, len(blocks), 2):
    link_tag = blocks[i]
    block_content = blocks[i+1]
    
    title_match = re.search(r'<span[^>]*>([^<]+)</span>', block_content)
    if title_match:
        title = title_match.group(1).strip()
        new_img = mappings.get(title)
        
        if new_img:
            # base layer image
            block_content = re.sub(r'<img src="[^"]+"', f'<img src="/src/assets/{new_img}"', block_content)
            
            # reveal layer background image
            block_content = re.sub(r'background-image:\s*url\(\'[^\']+\'\)', f"background-image: url('/src/assets/{new_img}')", block_content)
            
    new_content += link_tag + block_content

with open(filename, 'w') as f:
    f.write(new_content)

print(f"Fixed {filename}")
