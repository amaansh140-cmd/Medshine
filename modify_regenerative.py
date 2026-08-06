import re

with open('treatment-regenerative.html', 'r') as f:
    content = f.read()

# Replace the title
content = re.sub(r'Medical Treatments', 'Regenerative Medicines', content)

# Create the new grid content
new_grid = """
            <div class="md:col-span-2 md:row-span-2 lg:col-span-2 lg:row-span-2 border border-ink/10 p-6 md:p-8 rounded-[24px] flex flex-col justify-center text-left reveal-anim bg-white/5 relative overflow-hidden group" >
              <span class="text-ink font-serif font-medium text-2xl md:text-3xl leading-snug mb-3">PRP (Platelet-Rich Plasma)</span>
              <p class="text-inkmute text-sm md:text-base leading-relaxed">Uses your own blood platelets, which release growth factors that support healing and tissue repair.</p>
            </div>

            <div class="md:col-span-2 md:row-span-2 lg:col-span-2 lg:row-span-2 border border-ink/10 p-6 md:p-8 rounded-[24px] flex flex-col justify-center text-left reveal-anim bg-white/5 relative overflow-hidden group" >
              <span class="text-ink font-serif font-medium text-2xl md:text-3xl leading-snug mb-3">PRF (Platelet-Rich Fibrin)</span>
              <p class="text-inkmute text-sm md:text-base leading-relaxed">A newer platelet concentrate that releases growth factors more gradually than PRP.</p>
            </div>

            <div class="md:col-span-2 md:row-span-2 lg:col-span-2 lg:row-span-2 border border-ink/10 p-6 md:p-8 rounded-[24px] flex flex-col justify-center text-left reveal-anim bg-white/5 relative overflow-hidden group" >
              <span class="text-ink font-serif font-medium text-2xl md:text-3xl leading-snug mb-3">Exosome therapy</span>
              <p class="text-inkmute text-sm md:text-base leading-relaxed">Uses extracellular vesicles that contain signaling molecules which may help with tissue repair and regeneration. Clinical research is ongoing, and regulatory approval varies by country.</p>
            </div>

            <div class="md:col-span-2 md:row-span-2 lg:col-span-2 lg:row-span-2 border border-ink/10 p-6 md:p-8 rounded-[24px] flex flex-col justify-center text-left reveal-anim bg-white/5 relative overflow-hidden group" >
              <span class="text-ink font-serif font-medium text-2xl md:text-3xl leading-snug mb-3">Regenera Activa</span>
              <p class="text-inkmute text-sm md:text-base leading-relaxed">Uses a small sample of your own scalp tissue to produce a suspension containing progenitor cells and growth factors for hair restoration.</p>
            </div>

            <div class="md:col-span-2 md:row-span-2 lg:col-span-2 lg:row-span-2 border border-ink/10 p-6 md:p-8 rounded-[24px] flex flex-col justify-center text-left reveal-anim bg-white/5 relative overflow-hidden group" >
              <span class="text-ink font-serif font-medium text-2xl md:text-3xl leading-snug mb-3">Autologous fat grafting (nanofat/microfat)</span>
              <p class="text-inkmute text-sm md:text-base leading-relaxed">Uses the patient's own fat, which contains regenerative cells and growth factors, for selected reconstructive and aesthetic indications.</p>
            </div>

            <div class="md:col-span-2 md:row-span-2 lg:col-span-2 lg:row-span-2 border border-ink/10 p-6 md:p-8 rounded-[24px] flex flex-col justify-center text-left reveal-anim bg-white/5 relative overflow-hidden group" >
              <span class="text-ink font-serif font-medium text-2xl md:text-3xl leading-snug mb-3">Stem cell-based therapies</span>
              <p class="text-inkmute text-sm md:text-base leading-relaxed">These are an active area of research. Many marketed cosmetic "stem cell" treatments are not supported by strong clinical evidence, and true stem cell therapies are regulated differently in many countries.</p>
            </div>
          </div>

          <div class="mt-16">
            <h2 class="font-serif font-medium leading-[0.95] tracking-tight text-ink mb-8 reveal-anim text-4xl">Applications</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
              <div class="border border-ink/10 p-4 rounded-xl text-ink font-medium reveal-anim text-center">Hair loss (androgenetic alopecia)</div>
              <div class="border border-ink/10 p-4 rounded-xl text-ink font-medium reveal-anim text-center">Skin rejuvenation</div>
              <div class="border border-ink/10 p-4 rounded-xl text-ink font-medium reveal-anim text-center">Acne scars</div>
              <div class="border border-ink/10 p-4 rounded-xl text-ink font-medium reveal-anim text-center">Wound healing</div>
              <div class="border border-ink/10 p-4 rounded-xl text-ink font-medium reveal-anim text-center">Orthopaedic injuries</div>
              <div class="border border-ink/10 p-4 rounded-xl text-ink font-medium reveal-anim text-center">Certain reconstructive procedures</div>
            </div>
"""

# Replace the grid content
pattern = r'<div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6 grid-flow-dense auto-rows-\[220px\] md:auto-rows-\[160px\]">.*?</div>\s*</section>'
content = re.sub(pattern, '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 grid-flow-dense">' + new_grid + '\n          </section>', content, flags=re.DOTALL)

with open('treatment-regenerative.html', 'w') as f:
    f.write(content)

