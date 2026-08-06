import re

with open('reviews.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I need to extract the 6 review divs.
# I'll just use regex to match '<!-- Review X --> ... </div>\n  </div>'
pattern = re.compile(r'<!-- Review \d+ -->.*?</div>\n    </div>\n  </div>', re.DOTALL)
reviews = pattern.findall(content)

if len(reviews) >= 6:
    # There are 12 reviews because we duplicated them for the slider.
    # We only need the first 6 unique ones.
    unique_reviews = reviews[:6]
    
    row1_reviews = unique_reviews[:3]
    row2_reviews = unique_reviews[3:]
    
    row1_html = "\n".join(row1_reviews)
    row1_duplicated = row1_html + "\n  <!-- Duplicates for seamless loop -->\n" + row1_html
    
    row2_html = "\n".join(row2_reviews)
    row2_duplicated = row2_html + "\n  <!-- Duplicates for seamless loop -->\n" + row2_html
    
    # Let's find the existing Slider Section
    start_marker = '<!-- Slider Section -->'
    end_marker = '</div>\n</div>'
    start_idx = content.find(start_marker)
    # The slider section ends with two closing divs. We need to be careful finding the end.
    # It's better to find '<div class="marquee-container' and the end of its parent.
    
    # Instead, let's just use string replacement for the entire block.
    # I'll search from start_marker to the next <script src="/src/main.js" type="module"></script>
    script_idx = content.find('<script src="/src/main.js"', start_idx)
    
    new_slider_section = f"""<!-- Slider Section -->
<div class="relative w-full max-w-[100vw] overflow-hidden py-4 -mx-6 md:-mx-10 px-6 md:px-10 flex flex-col gap-6 md:gap-8">
  <!-- Gradient fades for edges -->
  <div class="absolute inset-y-0 left-0 w-12 md:w-32 bg-gradient-to-r from-cream to-transparent z-10 pointer-events-none"></div>
  <div class="absolute inset-y-0 right-0 w-12 md:w-32 bg-gradient-to-l from-cream to-transparent z-10 pointer-events-none"></div>
  
  <!-- Row 1 (Slides Left) -->
  <div class="marquee-container gap-6 md:gap-8 hover:[animation-play-state:paused]" style="animation-duration: 35s;">
    {row1_duplicated}
  </div>

  <!-- Row 2 (Slides Right via reverse direction) -->
  <div class="marquee-container gap-6 md:gap-8 hover:[animation-play-state:paused]" style="animation-duration: 45s; animation-direction: reverse;">
    {row2_duplicated}
  </div>
</div>
"""
    
    new_content = content[:start_idx] + new_slider_section + "\n" + content[script_idx:]
    
    with open('reviews.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated reviews.html with 2 rows of sliders!")
else:
    print(f"Could not find 6 reviews. Found {len(reviews)}.")

