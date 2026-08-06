import re

with open("results.html", "r", encoding="utf-8") as f:
    content = f.read()

# We need to replace the FIRST result block.
# The first result block looks like this:
#   <!-- Result 1 -->
#   <div class="flex flex-col gap-6 group reveal-anim">
#     ...
#     </div>
#   </div>

# Wait, there are multiple results. Let's just find "<!-- Result 1 -->" and the next "<!-- Result 2 -->".
start_idx = content.find("<!-- Result 1 -->")
end_idx = content.find("<!-- Result 2 -->")

if start_idx != -1 and end_idx != -1:
    new_result = """<!-- Result 1 -->
  <div class="flex flex-col gap-6 group reveal-anim">
    
    <div class="relative w-full aspect-[4/3] rounded-[24px] overflow-hidden group/slider">
      <!-- After Image -->
      <img src="/src/assets/after_1.jpg" alt="After Treatment" class="absolute inset-0 w-full h-full object-cover" />
      
      <!-- Before Image Container (clipped) -->
      <img src="/src/assets/before_1.jpg" alt="Before Treatment" class="absolute inset-0 w-full h-full object-cover [clip-path:polygon(0_0,var(--split,50%)_0,var(--split,50%)_100%,0_100%)]" id="ba-image-1" />

      <!-- Range Input for dragging -->
      <input type="range" min="0" max="100" value="50" class="absolute inset-0 w-full h-full opacity-0 cursor-ew-resize z-20" oninput="document.getElementById('ba-image-1').style.setProperty('--split', this.value + '%'); document.getElementById('ba-handle-1').style.left = this.value + '%';" />

      <!-- Visual Handle -->
      <div id="ba-handle-1" class="absolute inset-y-0 left-1/2 w-1 bg-white/80 pointer-events-none z-10 -ml-[2px]">
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-8 h-8 bg-white rounded-full flex items-center justify-center shadow-lg shadow-black/20 text-ink">
          <!-- Left arrow -->
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="-ml-0.5"><path d="M15 18l-6-6 6-6"/></svg>
          <!-- Right arrow -->
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="-mr-0.5"><path d="M9 18l6-6-6-6"/></svg>
        </div>
      </div>
      
      <!-- Badges -->
      <div class="absolute top-4 left-4 bg-ink/70 backdrop-blur-md px-3 py-1.5 rounded-full text-cream text-[10px] font-bold uppercase tracking-widest z-10 opacity-0 group-hover/slider:opacity-100 transition-opacity pointer-events-none">Before</div>
      <div class="absolute top-4 right-4 bg-ink/70 backdrop-blur-md px-3 py-1.5 rounded-full text-cream text-[10px] font-bold uppercase tracking-widest z-10 opacity-0 group-hover/slider:opacity-100 transition-opacity pointer-events-none">After</div>
    </div>

    <div class="flex flex-col gap-2">
      <h3 class="font-serif text-2xl font-semibold text-ink leading-tight">Pigmentation & Skin Texture</h3>
      <p class="text-inkmute font-light leading-relaxed">Noticeable improvement in skin tone, reduction of dark spots, and overall rejuvenation using our customized clinical protocols.</p>
    </div>
  </div>

  """
    
    new_content = content[:start_idx] + new_result + content[end_idx:]
    with open("results.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Added before/after slider to results.html!")
else:
    print("Could not find Result 1 markers.")
