import re
import shutil

treatments = [
    ("PRP (Platelet-Rich Plasma)", "treatment-regenerative-prp.html", "md:col-span-2 md:row-span-2 lg:col-span-2 lg:row-span-2"),
    ("PRF (Platelet-Rich Fibrin)", "treatment-regenerative-prf.html", "md:col-span-1 md:row-span-2 lg:col-span-1 lg:row-span-2"),
    ("Exosome therapy", "treatment-regenerative-exosome.html", "md:col-span-1 md:row-span-1 lg:col-span-1 lg:row-span-1"),
    ("Regenera Activa", "treatment-regenerative-regenera-activa.html", "md:col-span-1 md:row-span-1 lg:col-span-1 lg:row-span-1"),
    ("Autologous fat grafting (nanofat/microfat)", "treatment-regenerative-autologous-fat.html", "md:col-span-2 md:row-span-1 lg:col-span-2 lg:row-span-1"),
    ("Stem cell-based therapies", "treatment-regenerative-stem-cell.html", "md:col-span-1 md:row-span-1 lg:col-span-1 lg:row-span-1")
]

with open('treatment-regenerative.html', 'r') as f:
    content = f.read()

# I will just replace the entire <div class="grid...">...</div> portion and the "Applications" section with a newly generated grid.
# There are two grids (base layer and reveal layer).

def generate_grid(is_reveal=False):
    html = '<div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6 grid-flow-dense auto-rows-[220px] md:auto-rows-[160px]">\n'
    for title, link, span_classes in treatments:
        border_color = "cream/10" if is_reveal else "ink/10"
        text_color = "cream" if is_reveal else "ink"
        
        html += f"""
            <a href="{link}" class="{span_classes} border border-{border_color} p-6 md:p-8 rounded-[24px] flex flex-col items-center justify-center text-center reveal-anim bg-white/5 relative overflow-hidden group" >
              <span class="text-{text_color} font-serif font-medium text-2xl md:text-3xl leading-snug">{title}</span>
            </a>
"""
    html += '          </div>\n        </section>'
    return html

# The regex matches everything from <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 grid-flow-dense"> to </section>
base_grid = generate_grid(is_reveal=False)
reveal_grid = generate_grid(is_reveal=True)

# Split by REVEAL LAYER
parts = content.split("<!-- REVEAL LAYER -->")

# Replace in base layer
pattern = r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 grid-flow-dense">.*?</section>'
parts[0] = re.sub(pattern, base_grid, parts[0], flags=re.DOTALL)

# Replace in reveal layer
if len(parts) > 1:
    parts[1] = re.sub(pattern, reveal_grid, parts[1], flags=re.DOTALL)

content = "<!-- REVEAL LAYER -->".join(parts)

with open('treatment-regenerative.html', 'w') as f:
    f.write(content)

