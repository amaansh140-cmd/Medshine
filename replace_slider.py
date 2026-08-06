import os
import shutil
import re

slider_html = """
<!-- Image Slider Section -->
<section class="max-w-[100vw] overflow-hidden mb-28 py-6">
  <div class="flex overflow-hidden group">
    <!-- First Set -->
    <div class="flex gap-6 animate-marquee group-hover:[animation-play-state:paused] pr-6 flex-none">
      
      <!-- Slide 1 -->
      <div class="w-[280px] md:w-[320px] flex-none bg-white rounded-[16px] overflow-hidden shadow-sm border border-ink/10 whitespace-normal">
        <div class="h-[300px] w-full relative">
          <img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?q=80&w=600&auto=format&fit=crop" alt="Clinic Interior" class="w-full h-full object-cover" />
        </div>
        <div class="p-6 text-left bg-white">
          <h3 class="font-sans font-bold text-ink text-[15px] uppercase tracking-wide mb-1">STATE-OF-THE-ART FACILITIES</h3>
          <p class="text-inkmute text-xs">Luxurious Clinical Environment</p>
        </div>
      </div>
      
      <!-- Slide 2 -->
      <div class="w-[280px] md:w-[320px] flex-none bg-white rounded-[16px] overflow-hidden shadow-sm border border-ink/10 whitespace-normal">
        <div class="h-[300px] w-full relative">
          <img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?q=80&w=600&auto=format&fit=crop" alt="Consultation" class="w-full h-full object-cover" />
        </div>
        <div class="p-6 text-left bg-white">
          <h3 class="font-sans font-bold text-ink text-[15px] uppercase tracking-wide mb-1">EXPERT CONSULTATION</h3>
          <p class="text-inkmute text-xs">Precision Diagnosis & Care</p>
        </div>
      </div>
      
      <!-- Slide 3 -->
      <div class="w-[280px] md:w-[320px] flex-none bg-white rounded-[16px] overflow-hidden shadow-sm border border-ink/10 whitespace-normal">
        <div class="h-[300px] w-full relative">
          <img src="https://images.unsplash.com/photo-1616394584738-fc6e612e71c9?q=80&w=600&auto=format&fit=crop" alt="Aesthetics" class="w-full h-full object-cover" />
        </div>
        <div class="p-6 text-left bg-white">
          <h3 class="font-sans font-bold text-ink text-[15px] uppercase tracking-wide mb-1">SUBTLE REJUVENATION</h3>
          <p class="text-inkmute text-xs">Non-Invasive Facial Aesthetics</p>
        </div>
      </div>

      <!-- Slide 4 -->
      <div class="w-[280px] md:w-[320px] flex-none bg-white rounded-[16px] overflow-hidden shadow-sm border border-ink/10 whitespace-normal">
        <div class="h-[300px] w-full relative">
          <img src="https://images.unsplash.com/photo-1582719508461-905c673771fd?q=80&w=600&auto=format&fit=crop" alt="Advanced Laser" class="w-full h-full object-cover" />
        </div>
        <div class="p-6 text-left bg-white">
          <h3 class="font-sans font-bold text-ink text-[15px] uppercase tracking-wide mb-1">ADVANCED LASER MEDICINE</h3>
          <p class="text-inkmute text-xs">Precision Fractional Therapy</p>
        </div>
      </div>

    </div>
    
    <!-- Second Set (Duplicate for seamless loop) -->
    <div class="flex gap-6 animate-marquee group-hover:[animation-play-state:paused] pr-6 flex-none" aria-hidden="true">
      
      <div class="w-[280px] md:w-[320px] flex-none bg-white rounded-[16px] overflow-hidden shadow-sm border border-ink/10 whitespace-normal">
        <div class="h-[300px] w-full relative">
          <img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?q=80&w=600&auto=format&fit=crop" alt="Clinic Interior" class="w-full h-full object-cover" />
        </div>
        <div class="p-6 text-left bg-white">
          <h3 class="font-sans font-bold text-ink text-[15px] uppercase tracking-wide mb-1">STATE-OF-THE-ART FACILITIES</h3>
          <p class="text-inkmute text-xs">Luxurious Clinical Environment</p>
        </div>
      </div>
      
      <div class="w-[280px] md:w-[320px] flex-none bg-white rounded-[16px] overflow-hidden shadow-sm border border-ink/10 whitespace-normal">
        <div class="h-[300px] w-full relative">
          <img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?q=80&w=600&auto=format&fit=crop" alt="Consultation" class="w-full h-full object-cover" />
        </div>
        <div class="p-6 text-left bg-white">
          <h3 class="font-sans font-bold text-ink text-[15px] uppercase tracking-wide mb-1">EXPERT CONSULTATION</h3>
          <p class="text-inkmute text-xs">Precision Diagnosis & Care</p>
        </div>
      </div>
      
      <div class="w-[280px] md:w-[320px] flex-none bg-white rounded-[16px] overflow-hidden shadow-sm border border-ink/10 whitespace-normal">
        <div class="h-[300px] w-full relative">
          <img src="https://images.unsplash.com/photo-1616394584738-fc6e612e71c9?q=80&w=600&auto=format&fit=crop" alt="Aesthetics" class="w-full h-full object-cover" />
        </div>
        <div class="p-6 text-left bg-white">
          <h3 class="font-sans font-bold text-ink text-[15px] uppercase tracking-wide mb-1">SUBTLE REJUVENATION</h3>
          <p class="text-inkmute text-xs">Non-Invasive Facial Aesthetics</p>
        </div>
      </div>

      <div class="w-[280px] md:w-[320px] flex-none bg-white rounded-[16px] overflow-hidden shadow-sm border border-ink/10 whitespace-normal">
        <div class="h-[300px] w-full relative">
          <img src="https://images.unsplash.com/photo-1582719508461-905c673771fd?q=80&w=600&auto=format&fit=crop" alt="Advanced Laser" class="w-full h-full object-cover" />
        </div>
        <div class="p-6 text-left bg-white">
          <h3 class="font-sans font-bold text-ink text-[15px] uppercase tracking-wide mb-1">ADVANCED LASER MEDICINE</h3>
          <p class="text-inkmute text-xs">Precision Fractional Therapy</p>
        </div>
      </div>

    </div>
  </div>
</section>
"""

target_files = ['index.html', 'dr-priya.html', 'dr-ankur.html']

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace the entire slider section
        content = re.sub(r'<!-- Image Slider Section -->.*?</section>', slider_html, content, flags=re.DOTALL)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        if os.path.exists(f'../Medshine/{filename}'):
            shutil.copy(filename, f'../Medshine/{filename}')

# Add CSS for continuous marquee
css = """
@keyframes marquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-100%); }
}
.animate-marquee {
  animation: marquee 25s linear infinite;
}
"""

with open('src/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()
    
if '.animate-marquee' not in css_content:
    with open('src/style.css', 'a', encoding='utf-8') as f:
        f.write(css)
        
    if os.path.exists('../Medshine/src/style.css'):
        shutil.copy('src/style.css', '../Medshine/src/style.css')

print("Slider updated to cards with infinite scroll!")
