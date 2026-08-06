import re
import shutil

treatments = [
    ("PRP (Platelet-Rich Plasma)", "treatment-regenerative-prp.html", "md:col-span-2 md:row-span-2 lg:col-span-2 lg:row-span-2", "treatment_prp_indian.jpg"),
    ("PRF (Platelet-Rich Fibrin)", "treatment-regenerative-prf.html", "md:col-span-1 md:row-span-2 lg:col-span-1 lg:row-span-2", "treatment_prf_indian.jpg"),
    ("Exosome therapy", "treatment-regenerative-exosome.html", "md:col-span-1 md:row-span-1 lg:col-span-1 lg:row-span-1", "treatment_exosome_indian.jpg"),
    ("Regenera Activa", "treatment-regenerative-regenera-activa.html", "md:col-span-1 md:row-span-1 lg:col-span-1 lg:row-span-1", "treatment_hair_new.jpg"),
    ("Autologous fat grafting (nanofat/microfat)", "treatment-regenerative-autologous-fat.html", "md:col-span-2 md:row-span-1 lg:col-span-2 lg:row-span-1", "treatment_non_surgical.jpg"),
    ("Stem cell-based therapies", "treatment-regenerative-stem-cell.html", "md:col-span-1 md:row-span-1 lg:col-span-1 lg:row-span-1", "treatment_medical_new.jpg")
]

with open('treatment-regenerative.html', 'r') as f:
    content = f.read()

def generate_reveal_grid():
    html = '<div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6 grid-flow-dense auto-rows-[220px] md:auto-rows-[160px]">\n'
    for title, link, span_classes, bg_img in treatments:
        html += f"""
            <a href="{link}" class="{span_classes} border border-cream/10 p-6 md:p-8 rounded-[24px] flex flex-col items-center justify-center text-center reveal-anim bg-white/5 relative overflow-hidden group" style="background-image: url('/src/assets/{bg_img}'); background-size: cover; background-position: center;">
              <div class="absolute inset-0 bg-ink/60 rounded-[24px]"></div>
              <span class="text-cream relative z-10 font-serif font-medium text-2xl md:text-3xl leading-snug">{title}</span>
            </a>
"""
    html += '          </div>\n        </section>'
    return html

reveal_grid = generate_reveal_grid()

# Split by REVEAL LAYER
parts = content.split("<!-- REVEAL LAYER -->")

# Replace in reveal layer
if len(parts) > 1:
    pattern = r'<div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6 grid-flow-dense auto-rows-\[220px\] md:auto-rows-\[160px\]">.*?</section>'
    parts[1] = re.sub(pattern, reveal_grid, parts[1], flags=re.DOTALL)

content = "<!-- REVEAL LAYER -->".join(parts)

with open('treatment-regenerative.html', 'w') as f:
    f.write(content)

shutil.copy('treatment-regenerative.html', '../Medshine/treatment-regenerative.html')

