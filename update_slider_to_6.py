import os
import shutil
import re

target_files = ['index.html', 'dr-priya.html', 'dr-ankur.html']

slides_html = """<div class="flex gap-4 md:gap-6 pr-4 md:pr-6 flex-none items-center" id="smooth-slider-track" style="will-change: transform;">
      
      <!-- Slide 1 -->
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="/public/clinic-room.jpg" alt="Clinic Interior" class="w-full h-full object-cover" />
      </div>
      
      <!-- Slide 2 -->
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="/public/laser-machine.jpg" alt="Laser Machine" class="w-full h-full object-cover" />
      </div>
      
      <!-- Slide 3 -->
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="/public/product-shelf.jpg" alt="Product Shelf" class="w-full h-full object-cover" />
      </div>

      <!-- Slide 4 -->
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="/public/face-exam.PNG" alt="Face Exam" class="w-full h-full object-cover" />
      </div>

      <!-- Slide 5 -->
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="/public/hair-treatment.PNG" alt="Hair Treatment" class="w-full h-full object-cover" />
      </div>

      <!-- Slide 6 -->
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="/public/desk-consult.PNG" alt="Consultation" class="w-full h-full object-cover" />
      </div>
      
      <!-- Duplicates for seamless loop -->
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="/public/clinic-room.jpg" alt="Clinic Interior" class="w-full h-full object-cover" />
      </div>
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="/public/laser-machine.jpg" alt="Laser Machine" class="w-full h-full object-cover" />
      </div>
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="/public/product-shelf.jpg" alt="Product Shelf" class="w-full h-full object-cover" />
      </div>
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="/public/face-exam.PNG" alt="Face Exam" class="w-full h-full object-cover" />
      </div>
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="/public/hair-treatment.PNG" alt="Hair Treatment" class="w-full h-full object-cover" />
      </div>
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="/public/desk-consult.PNG" alt="Consultation" class="w-full h-full object-cover" />
      </div>
      
    </div>"""

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace the track div
        content = re.sub(r'<div class="flex gap-4 md:gap-6 pr-4 md:pr-6 flex-none items-center" id="smooth-slider-track".*?</div>\s*</div>', slides_html + '\n  </div>', content, flags=re.DOTALL)
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
                
        if os.path.exists(f'../Medshine/{filename}'):
            shutil.copy(filename, f'../Medshine/{filename}')

print("Slider expanded and updated with 6 custom images!")
