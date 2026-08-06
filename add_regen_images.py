import re
import os
import shutil
import glob

# 1. Find the latest generated images and copy them to src/assets and Medshine/src/assets
brain_dir = "/Users/amaanshaikh/.gemini/antigravity/brain/b217ac84-2eca-437a-b49b-85def1969909"
assets_dir = "src/assets"
medshine_assets_dir = "../Medshine/src/assets"

mapping = {
    "exosome": "treatment-regenerative-exosome.html",
    "fat": "treatment-regenerative-autologous-fat.html",
    "prf": "treatment-regenerative-prf.html",
    "prp": "treatment-regenerative-prp.html",
    "regenera": "treatment-regenerative-regenera-activa.html",
    "stemcell": "treatment-regenerative-stem-cell.html"
}

for key, html_file in mapping.items():
    # Find the image
    matches = glob.glob(os.path.join(brain_dir, f"treatment_regen_{key}_*.jpg"))
    if not matches:
        print(f"Could not find image for {key}")
        continue
    
    img_path = matches[0]
    dest_name = f"treatment_regen_{key}.jpg"
    dest_path = os.path.join(assets_dir, dest_name)
    medshine_dest_path = os.path.join(medshine_assets_dir, dest_name)
    
    # Copy files
    shutil.copy(img_path, dest_path)
    shutil.copy(img_path, medshine_dest_path)
    print(f"Copied {img_path} to {dest_path} and {medshine_dest_path}")
    
    # Update HTML file
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Base layer image block
    base_img = f"""
          <div class="aspect-video w-full rounded-[24px] border border-ink/10 mb-12 flex items-center justify-center reveal-anim overflow-hidden">
             <img src="/src/assets/{dest_name}" alt="Treatment Image" class="w-full h-full object-cover">
          </div>"""
          
    # Reveal layer image block
    reveal_img = f"""
          <div class="aspect-video w-full rounded-[24px] border border-cream/10 mb-12 flex items-center justify-center reveal-anim overflow-hidden">
             <img src="/src/assets/{dest_name}" alt="Treatment Image" class="w-full h-full object-cover grayscale opacity-90">
          </div>"""

    # We need to insert these right after the </h1> tag.
    # Split by REVEAL LAYER
    parts = content.split("<!-- REVEAL LAYER -->")
    
    if len(parts) == 2:
        # Base layer replacement
        parts[0] = re.sub(r'(</h1>)', r'\1' + base_img, parts[0])
        # Reveal layer replacement
        parts[1] = re.sub(r'(</h1>)', r'\1' + reveal_img, parts[1])
        
        new_content = "<!-- REVEAL LAYER -->".join(parts)
        
        with open(html_file, 'w') as f:
            f.write(new_content)
        
        shutil.copy(html_file, f"../Medshine/{html_file}")
        print(f"Updated {html_file}")
    else:
        print(f"Failed to process {html_file}")

