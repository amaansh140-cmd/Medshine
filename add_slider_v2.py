import os
import shutil

slider_html = """
<!-- Image Slider Section -->
<section class="max-w-[100vw] overflow-hidden mb-28">
  <div class="flex overflow-x-auto snap-x snap-mandatory gap-6 px-6 md:px-10 pb-8 no-scrollbar" style="scroll-padding-left: 1.5rem; scroll-padding-right: 1.5rem;">
    
    <!-- Slide 1 -->
    <div class="snap-center shrink-0 w-[85vw] md:w-[60vw] lg:w-[45vw] h-[350px] md:h-[500px] relative rounded-[32px] overflow-hidden group">
      <img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?q=80&w=1200&auto=format&fit=crop" alt="Clinic Interior" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-105" />
      <div class="absolute inset-0 bg-gradient-to-t from-ink/80 via-ink/20 to-transparent"></div>
      <div class="absolute bottom-8 left-8 right-8 md:bottom-12 md:left-12 md:right-12">
        <span class="text-cream/70 uppercase text-xs tracking-[0.28em] font-semibold block mb-3">Our Clinic</span>
        <h3 class="text-cream font-serif text-3xl md:text-4xl font-medium mb-3">State-of-the-Art Facilities</h3>
        <p class="text-cream/90 text-sm md:text-base max-w-[45ch]">Experience world-class dermatological care in our luxurious, highly advanced clinical environment.</p>
      </div>
    </div>
    
    <!-- Slide 2 -->
    <div class="snap-center shrink-0 w-[85vw] md:w-[60vw] lg:w-[45vw] h-[350px] md:h-[500px] relative rounded-[32px] overflow-hidden group">
      <img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?q=80&w=1200&auto=format&fit=crop" alt="Consultation" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-105" />
      <div class="absolute inset-0 bg-gradient-to-t from-ink/80 via-ink/20 to-transparent"></div>
      <div class="absolute bottom-8 left-8 right-8 md:bottom-12 md:left-12 md:right-12">
        <span class="text-cream/70 uppercase text-xs tracking-[0.28em] font-semibold block mb-3">Expert Care</span>
        <h3 class="text-cream font-serif text-3xl md:text-4xl font-medium mb-3">Precision Diagnosis</h3>
        <p class="text-cream/90 text-sm md:text-base max-w-[45ch]">We believe in empathetic medical care tailored to your unique skin profile and internal health.</p>
      </div>
    </div>
    
    <!-- Slide 3 -->
    <div class="snap-center shrink-0 w-[85vw] md:w-[60vw] lg:w-[45vw] h-[350px] md:h-[500px] relative rounded-[32px] overflow-hidden group">
      <img src="https://images.unsplash.com/photo-1616394584738-fc6e612e71c9?q=80&w=1200&auto=format&fit=crop" alt="Aesthetics" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-105" />
      <div class="absolute inset-0 bg-gradient-to-t from-ink/80 via-ink/20 to-transparent"></div>
      <div class="absolute bottom-8 left-8 right-8 md:bottom-12 md:left-12 md:right-12">
        <span class="text-cream/70 uppercase text-xs tracking-[0.28em] font-semibold block mb-3">Aesthetics</span>
        <h3 class="text-cream font-serif text-3xl md:text-4xl font-medium mb-3">Subtle Rejuvenation</h3>
        <p class="text-cream/90 text-sm md:text-base max-w-[45ch]">Non-invasive treatments designed to lift, hydrate, and restore your natural, youthful proportions.</p>
      </div>
    </div>

  </div>
</section>
"""

# Files to update
target_files = ['index.html', 'dr-priya.html', 'dr-ankur.html']

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        if "<!-- Biography & Credentials Grid -->" in content and "<!-- Image Slider Section -->" not in content:
            content = content.replace("<!-- Biography & Credentials Grid -->", slider_html + "\n<!-- Biography & Credentials Grid -->")
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
                
            if os.path.exists(f'../Medshine/{filename}'):
                shutil.copy(filename, f'../Medshine/{filename}')

# Append no-scrollbar css to style.css
with open('src/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()
    
if '.no-scrollbar' not in css_content:
    with open('src/style.css', 'a', encoding='utf-8') as f:
        f.write("\n/* Hide scrollbar */\n.no-scrollbar::-webkit-scrollbar { display: none; }\n.no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }\n")
        
    if os.path.exists('../Medshine/src/style.css'):
        shutil.copy('src/style.css', '../Medshine/src/style.css')

print("Slider injected successfully!")
