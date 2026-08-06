import re

with open("reviews.html", "r", encoding="utf-8") as f:
    content = f.read()

# Define the new review HTMLs
reviews_html = """
  <!-- Review 1 -->
  <div class="bg-ink/5 border border-ink/10 rounded-[24px] p-8 flex flex-col gap-6 reveal-anim hover-scale">
    <div class="flex gap-1 text-ink">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
    </div>
    <p class="text-ink text-sm leading-relaxed italic flex-1">"Best clinic for skin treatment. I did my pigmentation treatment with Dr. Priya and I got amazing results within a few sessions. Highly recommended for pigmentation."</p>
    <div class="flex items-center gap-4 border-t border-ink/10 pt-6">
      <div class="w-10 h-10 rounded-full bg-ink flex items-center justify-center text-cream font-serif font-medium text-lg">V</div>
      <div class="flex flex-col">
        <span class="text-ink font-medium text-sm">Vinod Tiwari</span>
        <span class="text-inkmute text-xs">Pigmentation Treatment</span>
      </div>
    </div>
  </div>

  <!-- Review 2 -->
  <div class="bg-ink/5 border border-ink/10 rounded-[24px] p-8 flex flex-col gap-6 reveal-anim hover-scale">
    <div class="flex gap-1 text-ink">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
    </div>
    <p class="text-ink text-sm leading-relaxed italic flex-1">"Absolutely loved my HydraFacial! My skin feels clean, soft, hydrated, and glowing. The treatment was painless and the results were instant!"</p>
    <div class="flex items-center gap-4 border-t border-ink/10 pt-6">
      <div class="w-10 h-10 rounded-full bg-ink flex items-center justify-center text-cream font-serif font-medium text-lg">K</div>
      <div class="flex flex-col">
        <span class="text-ink font-medium text-sm">Krutika Sawant</span>
        <span class="text-inkmute text-xs">HydraFacial</span>
      </div>
    </div>
  </div>

  <!-- Review 3 -->
  <div class="bg-ink/5 border border-ink/10 rounded-[24px] p-8 flex flex-col gap-6 reveal-anim hover-scale">
    <div class="flex gap-1 text-ink">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
    </div>
    <p class="text-ink text-sm leading-relaxed italic flex-1">"One of the finest clinics I have ever visited… really enjoyed the session. I went for Q switch treatment, had a great experience and loved the service and hospitality."</p>
    <div class="flex items-center gap-4 border-t border-ink/10 pt-6">
      <div class="w-10 h-10 rounded-full bg-ink flex items-center justify-center text-cream font-serif font-medium text-lg">R</div>
      <div class="flex flex-col">
        <span class="text-ink font-medium text-sm">Ranjith Poojary</span>
        <span class="text-inkmute text-xs">Q Switch Laser</span>
      </div>
    </div>
  </div>

  <!-- Review 4 -->
  <div class="bg-ink/5 border border-ink/10 rounded-[24px] p-8 flex flex-col gap-6 reveal-anim hover-scale">
    <div class="flex gap-1 text-ink">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
    </div>
    <p class="text-ink text-sm leading-relaxed italic flex-1">"I was having Face hyperpigmentation and took treatment with Dr. Priya mam at MediiDermashiine Clinic. I can safely say that Dr. Priya is the best skin doctor in Mumbai."</p>
    <div class="flex items-center gap-4 border-t border-ink/10 pt-6">
      <div class="w-10 h-10 rounded-full bg-ink flex items-center justify-center text-cream font-serif font-medium text-lg">S</div>
      <div class="flex flex-col">
        <span class="text-ink font-medium text-sm">Shubham Dubey</span>
        <span class="text-inkmute text-xs">Hyperpigmentation</span>
      </div>
    </div>
  </div>

  <!-- Review 5 -->
  <div class="bg-ink/5 border border-ink/10 rounded-[24px] p-8 flex flex-col gap-6 reveal-anim hover-scale">
    <div class="flex gap-1 text-ink">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
    </div>
    <p class="text-ink text-sm leading-relaxed italic flex-1">"I had went through a hair fall issue and went to mediidermashiine clinic and got a exosome treatment. Got very good hair growth in a couple of sessions. Highly recommend, best skin & hair clinic in Mumbai."</p>
    <div class="flex items-center gap-4 border-t border-ink/10 pt-6">
      <div class="w-10 h-10 rounded-full bg-ink flex items-center justify-center text-cream font-serif font-medium text-lg">S</div>
      <div class="flex flex-col">
        <span class="text-ink font-medium text-sm">Shiva Pandey</span>
        <span class="text-inkmute text-xs">Exosome Hair Treatment</span>
      </div>
    </div>
  </div>

  <!-- Review 6 -->
  <div class="bg-ink/5 border border-ink/10 rounded-[24px] p-8 flex flex-col gap-6 reveal-anim hover-scale">
    <div class="flex gap-1 text-ink">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
    </div>
    <p class="text-ink text-sm leading-relaxed italic flex-1">"Welcoming environment and expert care. I’ve seen a huge improvement in my skin since starting my treatments here."</p>
    <div class="flex items-center gap-4 border-t border-ink/10 pt-6">
      <div class="w-10 h-10 rounded-full bg-ink flex items-center justify-center text-cream font-serif font-medium text-lg">J</div>
      <div class="flex flex-col">
        <span class="text-ink font-medium text-sm">Janet Thoppil</span>
        <span class="text-inkmute text-xs">Skin Care</span>
      </div>
    </div>
  </div>
"""

start_marker = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 stagger-group">'
end_marker = '</section>'
start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx + len(start_marker)] + "\n" + reviews_html + "\n</div>\n" + content[end_idx:]
    with open("reviews.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated reviews.html successfully!")
else:
    print("Could not find the target section to replace.")
