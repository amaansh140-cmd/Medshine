import re

filename = "treatment-hair.html"

# Mappings of titles to their new image names
mappings = {
    "High Frequency Laser Helmet": "treatment_hair_laser_helmet.jpg",
    "Platelet Rich Plasma Therapy (PRP)": "treatment_hair_prp.jpg",
    "Anti Dandruff Treatments": "treatment_hair_anti_dandruff.jpg",
    "MesoTherapy": "treatment_hair_mesotherapy.jpg",
    "QR678": "treatment_hair_qr678.jpg",
    "Derma Rollers": "treatment_hair_derma_rollers.jpg",
    "Scalp Treatment": "treatment_hair_scalp_treatment.jpg",
    "Hair meso": "treatment_hair_meso.jpg",
    "Hair analysis": "treatment_hair_analysis.jpg"
}

with open(filename, 'r') as f:
    content = f.read()

# Each treatment block has an <img> followed by some divs and then the <h2>title</h2>
# Example:
# <img src="/src/assets/treatment_hair_indian.jpg" alt="Treatment" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
# ...
# <h2 class="text-xl md:text-2xl font-serif text-cream mb-4">High Frequency Laser Helmet</h2>

# We will split by treatment blocks (the <a href="treatment-hair-...> tags)
blocks = re.split(r'(<a href="treatment-hair-[a-z0-9-]+\.html")', content)

new_content = blocks[0]

for i in range(1, len(blocks), 2):
    link_tag = blocks[i]
    block_content = blocks[i+1]
    
    # Identify the title
    title_match = re.search(r'<h2[^>]*>(.*?)</h2>', block_content)
    if title_match:
        title = title_match.group(1).strip()
        
        # Check against mappings
        new_img = mappings.get(title)
        if new_img:
            # Replace the img src for this block
            # Since the block might have an img tag, we replace its src
            block_content = re.sub(r'<img src="[^"]+"', f'<img src="/src/assets/{new_img}"', block_content, count=1)
            
    new_content += link_tag + block_content

with open(filename, 'w') as f:
    f.write(new_content)

print(f"Updated {filename}")
