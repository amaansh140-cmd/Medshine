import re

filename = "treatment-hair.html"

mappings = {
    "High Frequency Laser Helmet": "treatment_hair_laser_helmet.jpg",
    "Platelet Rich Plasma Therapy (PRP)": "treatment_hair_prp.jpg",
    "Anti Dandruff Treatments": "treatment_hair_anti_dandruff.jpg",
    "MesoTherapy": "treatment_hair_mesotherapy.jpg",
    "QR678": "treatment_hair_qr678.jpg",
    "Derma Rollers": "treatment_hair_derma_rollers.jpg",
    "Scalp Treatment": "treatment_hair_scalp_treatment.jpg",
    "Hair meso": "treatment_hair_meso.jpg",
    "Hair analysis": "treatment_hair_analysis.jpg",
    "Platelet Rich Plasma Therapy": "treatment_hair_prp.jpg", # alternative name
}

with open(filename, 'r') as f:
    content = f.read()

# Split by the blocks that contain the title
blocks = re.split(r'(<a href="treatment-hair-[a-z0-9-]+\.html")', content)

new_content = blocks[0]

for i in range(1, len(blocks), 2):
    link_tag = blocks[i]
    block_content = blocks[i+1]
    
    # Check for span title
    title_match = re.search(r'<span[^>]*>([^<]+)</span>', block_content)
    if title_match:
        title = title_match.group(1).strip()
        new_img = mappings.get(title)
        
        if new_img:
            # base layer image
            block_content = re.sub(r'<img src="[^"]+"', f'<img src="/src/assets/{new_img}"', block_content)
            
            # reveal layer background image (which is right inside block_content, since we split on `<a href=...`)
            block_content = re.sub(r'background-image:\s*url\(\'[^\']+\'\)', f"background-image: url('/src/assets/{new_img}')", block_content)
            
    new_content += link_tag + block_content

with open(filename, 'w') as f:
    f.write(new_content)

print(f"Fixed {filename}")
