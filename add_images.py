import re
import shutil

treatments = [
    {
        "file": "treatment-regenerative-prp.html",
        "image": "treatment_prp_indian.jpg"
    },
    {
        "file": "treatment-regenerative-prf.html",
        "image": "treatment_prf_indian.jpg"
    },
    {
        "file": "treatment-regenerative-exosome.html",
        "image": "treatment_exosome_indian.jpg"
    },
    {
        "file": "treatment-regenerative-regenera-activa.html",
        "image": "treatment_hair_new.jpg"
    },
    {
        "file": "treatment-regenerative-autologous-fat.html",
        "image": "treatment_non_surgical.jpg"
    },
    {
        "file": "treatment-regenerative-stem-cell.html",
        "image": "treatment_medical_new.jpg"
    }
]

for t in treatments:
    with open(t["file"], 'r') as f:
        content = f.read()
    
    # We want to add the image block immediately after the </h1> tag
    # The image block looks like:
    # <div class="aspect-video w-full rounded-[24px] border border-ink/10 mb-12 flex items-center justify-center reveal-anim overflow-hidden">
    #    <img src="/src/assets/IMAGE" alt="Treatment" class="w-full h-full object-cover">
    # </div>
    
    # Base layer (ink)
    img_block_base = f'''
          <div class="aspect-video w-full rounded-[24px] border border-ink/10 mb-12 flex items-center justify-center reveal-anim overflow-hidden">
             <img src="/src/assets/{t["image"]}" alt="Treatment" class="w-full h-full object-cover">
          </div>'''
          
    # Reveal layer (cream)
    img_block_reveal = f'''
          <div class="aspect-video w-full rounded-[24px] border border-cream/10 mb-12 flex items-center justify-center reveal-anim overflow-hidden">
             <img src="/src/assets/{t["image"]}" alt="Treatment" class="w-full h-full object-cover grayscale opacity-90">
          </div>'''

    parts = content.split("<!-- REVEAL LAYER -->")
    
    # Update base layer
    parts[0] = re.sub(r'(</h1>)', r'\1' + img_block_base, parts[0])
    
    # Update reveal layer
    if len(parts) > 1:
        parts[1] = re.sub(r'(</h1>)', r'\1' + img_block_reveal, parts[1])
        
    content = "<!-- REVEAL LAYER -->".join(parts)
    
    with open(t["file"], 'w') as f:
        f.write(content)
        
    shutil.copy(t["file"], f'../Medshine/{t["file"]}')

