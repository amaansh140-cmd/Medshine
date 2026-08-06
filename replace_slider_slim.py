import os
import shutil
import re

slider_html = """
<!-- Image Slider Section -->
<section class="max-w-[100vw] overflow-hidden mb-28 py-6">
  <div class="flex overflow-hidden group">
    <!-- First Set -->
    <div class="flex gap-4 md:gap-6 animate-marquee group-hover:[animation-play-state:paused] pr-4 md:pr-6 flex-none">
      
      <!-- Slide 1 -->
      <div class="w-[200px] md:w-[240px] h-[360px] md:h-[480px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?q=80&w=600&auto=format&fit=crop" alt="Clinic Interior" class="w-full h-full object-cover" />
      </div>
      
      <!-- Slide 2 -->
      <div class="w-[200px] md:w-[240px] h-[360px] md:h-[480px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?q=80&w=600&auto=format&fit=crop" alt="Consultation" class="w-full h-full object-cover" />
      </div>
      
      <!-- Slide 3 -->
      <div class="w-[200px] md:w-[240px] h-[360px] md:h-[480px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1616394584738-fc6e612e71c9?q=80&w=600&auto=format&fit=crop" alt="Aesthetics" class="w-full h-full object-cover" />
      </div>

      <!-- Slide 4 -->
      <div class="w-[200px] md:w-[240px] h-[360px] md:h-[480px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1582719508461-905c673771fd?q=80&w=600&auto=format&fit=crop" alt="Advanced Laser" class="w-full h-full object-cover" />
      </div>

      <!-- Slide 5 (Extra for smoother loop) -->
      <div class="w-[200px] md:w-[240px] h-[360px] md:h-[480px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1512290923902-8a9f81dc236c?q=80&w=600&auto=format&fit=crop" alt="Skin Care" class="w-full h-full object-cover" />
      </div>

    </div>
    
    <!-- Second Set (Duplicate for seamless loop) -->
    <div class="flex gap-4 md:gap-6 animate-marquee group-hover:[animation-play-state:paused] pr-4 md:pr-6 flex-none" aria-hidden="true">
      
      <div class="w-[200px] md:w-[240px] h-[360px] md:h-[480px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?q=80&w=600&auto=format&fit=crop" alt="Clinic Interior" class="w-full h-full object-cover" />
      </div>
      
      <div class="w-[200px] md:w-[240px] h-[360px] md:h-[480px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?q=80&w=600&auto=format&fit=crop" alt="Consultation" class="w-full h-full object-cover" />
      </div>
      
      <div class="w-[200px] md:w-[240px] h-[360px] md:h-[480px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1616394584738-fc6e612e71c9?q=80&w=600&auto=format&fit=crop" alt="Aesthetics" class="w-full h-full object-cover" />
      </div>

      <div class="w-[200px] md:w-[240px] h-[360px] md:h-[480px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1582719508461-905c673771fd?q=80&w=600&auto=format&fit=crop" alt="Advanced Laser" class="w-full h-full object-cover" />
      </div>

      <div class="w-[200px] md:w-[240px] h-[360px] md:h-[480px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1512290923902-8a9f81dc236c?q=80&w=600&auto=format&fit=crop" alt="Skin Care" class="w-full h-full object-cover" />
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

print("Slider updated to slim vertical poster format!")
