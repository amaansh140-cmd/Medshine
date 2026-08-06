import re

with open("blog.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace title
content = re.sub(r'<title>.*?</title>', '<title>Clinical Results | Medshine Clinic</title>', content)

# We want to replace everything from <section class="max-w-[1240px] mx-auto px-6 md:px-10 pt-32 pb-32">
# to its closing </section> with our new results section.
section_start = content.find('<section class="max-w-[1240px] mx-auto px-6 md:px-10 pt-32 pb-32">')
section_end = content.find('</section>', section_start) + len('</section>')

new_section = """<section class="max-w-[1240px] mx-auto px-6 md:px-10 pt-32 pb-32">
<div class="flex flex-col items-center text-center mb-16 reveal-anim">
<span class="text-ink uppercase text-xs tracking-[0.28em] font-semibold mb-4">Before & After</span>
<h1 class="font-serif font-medium leading-[0.95] tracking-tight text-ink mb-6 reveal-fade" style="font-size: clamp(2.8rem, 8vw, 4.8rem);">
  Clinical <em class="font-light italic text-inkmute">Transformations</em>
</h1>
<p class="text-inkmute font-light max-w-[60ch] mx-auto">Explore authentic clinical results from our patients. At Medshine Clinic, we believe in evidence-based treatments that deliver visible, natural-looking transformations.</p>
</div>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-12 stagger-group">
  
  <!-- Result 1 -->
  <div class="flex flex-col gap-6 group reveal-anim">
    <div class="aspect-[4/3] w-full rounded-[24px] overflow-hidden border border-ink/10 bg-ink/5 relative">
      <div class="absolute top-4 left-4 bg-cream/90 backdrop-blur-md px-4 py-2 rounded-full z-10 border border-ink/10">
        <span class="text-xs uppercase tracking-widest text-ink font-semibold">Pigmentation</span>
      </div>
      <img alt="Pigmentation Treatment Result" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 reveal-fade" src="/src/assets/treatment_laser_pigmentation.jpg"/>
    </div>
    <div class="flex flex-col gap-2">
      <h3 class="font-serif text-2xl font-semibold text-ink leading-tight">Q-Switch Laser Toning</h3>
      <p class="text-inkmute font-light leading-relaxed">Significant reduction in melasma and deep pigmentation after 6 customized laser toning sessions combined with medical-grade topical treatments.</p>
    </div>
  </div>

  <!-- Result 2 -->
  <div class="flex flex-col gap-6 group reveal-anim">
    <div class="aspect-[4/3] w-full rounded-[24px] overflow-hidden border border-ink/10 bg-ink/5 relative">
      <div class="absolute top-4 left-4 bg-cream/90 backdrop-blur-md px-4 py-2 rounded-full z-10 border border-ink/10">
        <span class="text-xs uppercase tracking-widest text-ink font-semibold">Hair Restoration</span>
      </div>
      <img alt="Hair PRP Result" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 reveal-fade" src="/src/assets/treatment_hair_prp.jpg"/>
    </div>
    <div class="flex flex-col gap-2">
      <h3 class="font-serif text-2xl font-semibold text-ink leading-tight">Advanced PRP Therapy</h3>
      <p class="text-inkmute font-light leading-relaxed">Visible increase in hair density and thickness at the crown area following a 4-month protocol of Platelet-Rich Plasma (PRP) therapy and nutritional support.</p>
    </div>
  </div>

  <!-- Result 3 -->
  <div class="flex flex-col gap-6 group reveal-anim">
    <div class="aspect-[4/3] w-full rounded-[24px] overflow-hidden border border-ink/10 bg-ink/5 relative">
      <div class="absolute top-4 left-4 bg-cream/90 backdrop-blur-md px-4 py-2 rounded-full z-10 border border-ink/10">
        <span class="text-xs uppercase tracking-widest text-ink font-semibold">Acne & Scars</span>
      </div>
      <img alt="Acne Treatment Result" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 reveal-fade" src="/src/assets/treatment_mnrf_indian.jpeg"/>
    </div>
    <div class="flex flex-col gap-2">
      <h3 class="font-serif text-2xl font-semibold text-ink leading-tight">MNRF Scar Revision</h3>
      <p class="text-inkmute font-light leading-relaxed">Improvement in deep rolling acne scars and overall skin texture using Microneedling Radiofrequency (MNRF) combined with hyaluronic acid boosters.</p>
    </div>
  </div>

  <!-- Result 4 -->
  <div class="flex flex-col gap-6 group reveal-anim">
    <div class="aspect-[4/3] w-full rounded-[24px] overflow-hidden border border-ink/10 bg-ink/5 relative">
      <div class="absolute top-4 left-4 bg-cream/90 backdrop-blur-md px-4 py-2 rounded-full z-10 border border-ink/10">
        <span class="text-xs uppercase tracking-widest text-ink font-semibold">Skin Rejuvenation</span>
      </div>
      <img alt="Skin Rejuvenation Result" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 reveal-fade" src="/src/assets/treatment_facial_new.jpg"/>
    </div>
    <div class="flex flex-col gap-2">
      <h3 class="font-serif text-2xl font-semibold text-ink leading-tight">Clinical HydraFacial</h3>
      <p class="text-inkmute font-light leading-relaxed">Instant restoration of skin hydration and radiance. The patient achieved a flawless, glass-skin effect before a major event using our signature medicated facial.</p>
    </div>
  </div>

</div>

<div class="mt-20 text-center reveal-anim">
  <p class="text-sm text-inkmute italic max-w-[60ch] mx-auto border-t border-ink/10 pt-8">
    *Disclaimer: The images shown above represent actual patients of Medshine Clinic. However, individual results may vary depending on skin type, genetics, adherence to post-care instructions, and the severity of the condition.
  </p>
</div>
</section>"""

new_content = content[:section_start] + new_section + content[section_end:]

with open("results.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Created results.html successfully!")
