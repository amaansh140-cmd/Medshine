import re
import glob

def fix_category(filename, mappings):
    with open(filename, 'r') as f:
        content = f.read()
    
    # Split by the blocks that contain the title
    pattern = r'(<a href="' + filename.replace('.html', '-') + r'[a-z0-9-]+\.html")'
    blocks = re.split(pattern, content)
    
    if len(blocks) == 1:
        return
        
    new_content = blocks[0]
    
    for i in range(1, len(blocks), 2):
        link_tag = blocks[i]
        block_content = blocks[i+1]
        
        title_match = re.search(r'<span[^>]*>([^<]+)</span>', block_content)
        if title_match:
            title = title_match.group(1).strip()
            new_img = mappings.get(title)
            
            if new_img:
                block_content = re.sub(r'<img src="[^"]+"', f'<img src="/src/assets/{new_img}"', block_content)
                block_content = re.sub(r'background-image:\s*url\(\'[^\']+\'\)', f"background-image: url('/src/assets/{new_img}')", block_content)
                
        new_content += link_tag + block_content

    with open(filename, 'w') as f:
        f.write(new_content)
    print(f"Fixed {filename}")

bridal_mappings = {
    "Skin Polishing": "treatment_bridal_skin_polishing.jpg",
    "Customised treatment": "treatment_bridal_customised.jpg"
}

nonsurgical_mappings = {
    "HIFU": "treatment_non_surgical_hifu.jpg",
    "MNRF": "treatment_non_surgical_mnrf.jpg"
}

fix_category("treatment-bridal.html", bridal_mappings)
fix_category("treatment-non-surgical.html", nonsurgical_mappings)

