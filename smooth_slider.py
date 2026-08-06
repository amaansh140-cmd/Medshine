import os
import shutil
import re

target_files = ['index.html', 'dr-priya.html', 'dr-ankur.html']

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # We will replace the entire <section class="max-w-[100vw] overflow-hidden mb-28 py-6 relative">
        # and inject the JS script right after it.
        
        slider_html = """<!-- Image Slider Section -->
<section class="max-w-[100vw] overflow-hidden mb-28 py-6 relative" id="hero-slider-section">
  <!-- Gradient Fades for edges -->
  <div class="absolute inset-y-0 left-0 w-12 md:w-32 bg-gradient-to-r from-cream to-transparent z-10 pointer-events-none"></div>
  <div class="absolute inset-y-0 right-0 w-12 md:w-32 bg-gradient-to-l from-cream to-transparent z-10 pointer-events-none"></div>
  
  <div class="flex overflow-hidden" id="smooth-slider-container">
    <div class="flex gap-4 md:gap-6 pr-4 md:pr-6 flex-none items-center" id="smooth-slider-track" style="will-change: transform;">
      
      <!-- Slide 1 -->
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?q=80&w=600&auto=format&fit=crop" alt="Clinic Interior" class="w-full h-full object-cover" />
      </div>
      
      <!-- Slide 2 -->
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?q=80&w=600&auto=format&fit=crop" alt="Consultation" class="w-full h-full object-cover" />
      </div>
      
      <!-- Slide 3 -->
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1616394584738-fc6e612e71c9?q=80&w=600&auto=format&fit=crop" alt="Aesthetics" class="w-full h-full object-cover" />
      </div>

      <!-- Slide 4 -->
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1582719508461-905c673771fd?q=80&w=600&auto=format&fit=crop" alt="Advanced Laser" class="w-full h-full object-cover" />
      </div>

      <!-- Slide 5 -->
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1512290923902-8a9f81dc236c?q=80&w=600&auto=format&fit=crop" alt="Skin Care" class="w-full h-full object-cover" />
      </div>
      
      <!-- Duplicates for seamless loop -->
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?q=80&w=600&auto=format&fit=crop" alt="Clinic Interior" class="w-full h-full object-cover" />
      </div>
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?q=80&w=600&auto=format&fit=crop" alt="Consultation" class="w-full h-full object-cover" />
      </div>
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1616394584738-fc6e612e71c9?q=80&w=600&auto=format&fit=crop" alt="Aesthetics" class="w-full h-full object-cover" />
      </div>
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1582719508461-905c673771fd?q=80&w=600&auto=format&fit=crop" alt="Advanced Laser" class="w-full h-full object-cover" />
      </div>
      <div class="w-[200px] md:w-[240px] h-[320px] md:h-[420px] flex-none bg-ink/5 rounded-[16px] overflow-hidden shadow-sm border border-ink/10">
        <img src="https://images.unsplash.com/photo-1512290923902-8a9f81dc236c?q=80&w=600&auto=format&fit=crop" alt="Skin Care" class="w-full h-full object-cover" />
      </div>
      
    </div>
  </div>
</section>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const track = document.getElementById("smooth-slider-track");
    const container = document.getElementById("hero-slider-section");
    if (!track || !container) return;
    
    let speed = 1.2; // base pixels per frame
    let currentSpeed = speed;
    let scrollPos = 0;
    let isHovered = false;
    
    container.addEventListener("mouseenter", () => { isHovered = true; });
    container.addEventListener("mouseleave", () => { isHovered = false; });
    // For touch devices
    container.addEventListener("touchstart", () => { isHovered = true; });
    container.addEventListener("touchend", () => { isHovered = false; });
    
    function animate() {
      if (isHovered) {
        currentSpeed = currentSpeed * 0.92; // smooth deceleration
      } else {
        currentSpeed = currentSpeed + (speed - currentSpeed) * 0.08; // smooth acceleration
      }
      
      scrollPos -= currentSpeed;
      
      // The track width is doubled, we reset at exactly half the track width
      const totalWidth = track.scrollWidth;
      const maxScroll = totalWidth / 2;
      
      if (Math.abs(scrollPos) >= maxScroll) {
        scrollPos += maxScroll;
      }
      
      track.style.transform = `translate3d(${scrollPos}px, 0, 0)`;
      requestAnimationFrame(animate);
    }
    
    requestAnimationFrame(animate);
  });
</script>"""

        # Locate the slider section using regex
        content = re.sub(r'<!-- Image Slider Section -->.*?</section>', slider_html, content, flags=re.DOTALL)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        if os.path.exists(f'../Medshine/{filename}'):
            shutil.copy(filename, f'../Medshine/{filename}')

print("Smooth JS slider added!")
