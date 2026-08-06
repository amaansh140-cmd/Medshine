import re

with open('reviews.html', 'r', encoding='utf-8') as f:
    content = f.read()

# First, let's extract all the individual review div blocks.
# A review block looks like this: <div class="bg-ink/5 border border-ink/10 rounded-[24px] p-8 flex flex-col gap-6 reveal-anim hover-scale"> ... </div>
review_pattern = re.compile(r'<!-- Review \d+ -->\s*<div class="bg-ink/5 border border-ink/10 rounded-\[24px\] p-8 flex flex-col gap-6 reveal-anim hover-scale">.*?</div>\n    </div>\n  </div>', re.DOTALL)
reviews = review_pattern.findall(content)

# Actually, the regex might be fragile because the divs are nested. 
# Let's extract the whole grid chunk instead.
grid_start = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 stagger-group">'
grid_idx = content.find(grid_start)

if grid_idx == -1:
    print("Could not find the grid container.")
    exit(1)

# Find the end of the grid.
section_end = content.find('</section>', grid_idx)

# Extract the inner HTML of the grid
inner_html = content[grid_idx + len(grid_start):section_end].strip()
# Remove the closing </div> of the grid
if inner_html.endswith('</div>'):
    inner_html = inner_html[:-6].strip()

# Now we need to modify the classes of the review cards to have a fixed width and no 'reveal-anim' because it might interfere with the marquee.
# Actually, the user's `style.css` doesn't mind `reveal-anim`, but `flex-none w-[320px] md:w-[450px]` is needed.
# Let's just do a string replacement on the review wrapper.
inner_html = inner_html.replace('bg-ink/5 border border-ink/10 rounded-[24px] p-8 flex flex-col gap-6 reveal-anim hover-scale', 'bg-ink/5 border border-ink/10 rounded-[24px] p-8 flex flex-col gap-6 flex-none w-[85vw] md:w-[450px] transition-transform duration-300 hover:-translate-y-2')

# Now duplicate the inner HTML for the seamless loop
duplicated_html = inner_html + "\n  <!-- Duplicates for seamless loop -->\n" + inner_html

# Build the new slider structure
new_structure = f"""
<!-- Slider Section -->
<div class="relative w-full max-w-[100vw] overflow-hidden py-4 -mx-6 md:-mx-10 px-6 md:px-10">
  <!-- Gradient fades for edges -->
  <div class="absolute inset-y-0 left-0 w-12 md:w-32 bg-gradient-to-r from-cream to-transparent z-10 pointer-events-none"></div>
  <div class="absolute inset-y-0 right-0 w-12 md:w-32 bg-gradient-to-l from-cream to-transparent z-10 pointer-events-none"></div>
  
  <div class="marquee-container gap-6 md:gap-8 hover:[animation-play-state:paused]" style="animation-duration: 40s;">
    {duplicated_html}
  </div>
</div>
"""

new_content = content[:grid_idx] + new_structure + "\n" + content[section_end:]

with open('reviews.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated reviews.html to use a slider!")
