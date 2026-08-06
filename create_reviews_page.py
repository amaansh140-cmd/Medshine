import re

with open("blog.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace title
content = re.sub(r'<title>.*?</title>', '<title>Patient Reviews | Medshine Clinic</title>', content)

# We want to replace everything from <section class="max-w-[1240px] mx-auto px-6 md:px-10 pt-32 pb-32">
# to its closing </section> with our new reviews section.
section_start = content.find('<section class="max-w-[1240px] mx-auto px-6 md:px-10 pt-32 pb-32">')
section_end = content.find('</section>', section_start) + len('</section>')

new_section = """<section class="max-w-[1240px] mx-auto px-6 md:px-10 pt-32 pb-32">
<div class="flex flex-col items-center text-center mb-16 reveal-anim">
<span class="text-ink uppercase text-xs tracking-[0.28em] font-semibold mb-4">Patient Experiences</span>
<h1 class="font-serif font-medium leading-[0.95] tracking-tight text-ink mb-6 reveal-fade" style="font-size: clamp(2.8rem, 8vw, 4.8rem);">
  What Our <em class="font-light italic text-inkmute">Patients Say</em>
</h1>
<p class="text-inkmute font-light max-w-[60ch] mx-auto">Read authentic stories and experiences from patients who have transformed their skin, hair, and overall wellness with Dr. Priya Jain at Medshine Clinic.</p>
</div>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 stagger-group">
  <!-- Review 1 -->
  <div class="bg-ink/5 border border-ink/10 rounded-[24px] p-8 flex flex-col gap-6 reveal-anim hover-scale">
    <div class="flex gap-1 text-ink">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
    </div>
    <p class="text-ink text-sm leading-relaxed italic flex-1">"Dr. Priya is incredibly knowledgeable and patient. I had severe pigmentation issues that bothered me for years. After a few sessions of the Q-switch laser toning, my skin has never looked better. The clinic is pristine and the staff is wonderful."</p>
    <div class="flex items-center gap-4 border-t border-ink/10 pt-6">
      <div class="w-10 h-10 rounded-full bg-ink flex items-center justify-center text-cream font-serif font-medium text-lg">A</div>
      <div class="flex flex-col">
        <span class="text-ink font-medium text-sm">Anjali M.</span>
        <span class="text-inkmute text-xs">Laser Toning</span>
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
    <p class="text-ink text-sm leading-relaxed italic flex-1">"I came in for hair fall issues. The diagnostic approach Dr. Priya uses is fascinating—she really tries to get to the root cause rather than just giving a temporary fix. The PRP sessions showed visible results within a few months."</p>
    <div class="flex items-center gap-4 border-t border-ink/10 pt-6">
      <div class="w-10 h-10 rounded-full bg-ink flex items-center justify-center text-cream font-serif font-medium text-lg">R</div>
      <div class="flex flex-col">
        <span class="text-ink font-medium text-sm">Rohan K.</span>
        <span class="text-inkmute text-xs">Hair Restoration</span>
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
    <p class="text-ink text-sm leading-relaxed italic flex-1">"One of the best aesthetic clinics in Mumbai! The entire team makes you feel so comfortable. I got the customized medicated facial before my wedding and my skin was glowing completely naturally. Thank you Medshine!"</p>
    <div class="flex items-center gap-4 border-t border-ink/10 pt-6">
      <div class="w-10 h-10 rounded-full bg-ink flex items-center justify-center text-cream font-serif font-medium text-lg">S</div>
      <div class="flex flex-col">
        <span class="text-ink font-medium text-sm">Sneha P.</span>
        <span class="text-inkmute text-xs">Bridal Skin Care</span>
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
    <p class="text-ink text-sm leading-relaxed italic flex-1">"I have been visiting Dr. Priya for my acne scar treatments. We combined MNRF with skin boosters. The results have been phenomenal. She is highly professional and never pushes unnecessary treatments."</p>
    <div class="flex items-center gap-4 border-t border-ink/10 pt-6">
      <div class="w-10 h-10 rounded-full bg-ink flex items-center justify-center text-cream font-serif font-medium text-lg">M</div>
      <div class="flex flex-col">
        <span class="text-ink font-medium text-sm">Mehul D.</span>
        <span class="text-inkmute text-xs">Acne Scar Revision</span>
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
    <p class="text-ink text-sm leading-relaxed italic flex-1">"I had a fantastic experience getting anti-aging treatments here. Dr. Priya has a very light hand when it comes to injectables. It looks incredibly natural—just a more refreshed version of myself."</p>
    <div class="flex items-center gap-4 border-t border-ink/10 pt-6">
      <div class="w-10 h-10 rounded-full bg-ink flex items-center justify-center text-cream font-serif font-medium text-lg">P</div>
      <div class="flex flex-col">
        <span class="text-ink font-medium text-sm">Priyanka V.</span>
        <span class="text-inkmute text-xs">Anti-Aging</span>
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
    <p class="text-ink text-sm leading-relaxed italic flex-1">"Excellent clinical care. The entire facility is highly hygienic and the technology used is clearly top-tier. Highly recommended for anyone seeking genuine clinical cosmetology services."</p>
    <div class="flex items-center gap-4 border-t border-ink/10 pt-6">
      <div class="w-10 h-10 rounded-full bg-ink flex items-center justify-center text-cream font-serif font-medium text-lg">K</div>
      <div class="flex flex-col">
        <span class="text-ink font-medium text-sm">Karan S.</span>
        <span class="text-inkmute text-xs">General Cosmetology</span>
      </div>
    </div>
  </div>
</div>
</section>"""

new_content = content[:section_start] + new_section + content[section_end:]

with open("reviews.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Created reviews.html successfully!")
