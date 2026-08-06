import re

with open('reviews.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Current structure:
# <section class="max-w-[1240px] mx-auto px-6 md:px-10 pt-32 pb-32">
# <div class="flex flex-col items-center text-center mb-16 reveal-anim">
# ...
# </div>
#
# <!-- Slider Section -->
# <div class="relative w-full max-w-[100vw] overflow-hidden py-4 -mx-6 md:-mx-10 px-6 md:px-10 flex flex-col gap-6 md:gap-8">

# I want to close the <section> before <!-- Slider Section -->
# and maybe wrap the slider section in a clean full-width div.

start_slider_marker = "<!-- Slider Section -->"

if start_slider_marker in content:
    # Split the content
    parts = content.split(start_slider_marker)
    
    # In parts[0], I should close the section. Let's replace 'pb-32' with 'pb-16' in the opening tag to reduce gap.
    parts[0] = parts[0].replace('pt-32 pb-32', 'pt-32 pb-8')
    parts[0] += "</section>\n\n<!-- Slider Section -->\n<section class=\"w-full overflow-hidden pb-32\">\n"
    
    # In parts[1], remove the negative margins from the slider div because it's now genuinely full width.
    # The div is: <div class="relative w-full max-w-[100vw] overflow-hidden py-4 -mx-6 md:-mx-10 px-6 md:px-10 flex flex-col gap-6 md:gap-8">
    parts[1] = parts[1].replace('-mx-6 md:-mx-10 px-6 md:px-10', 'px-0')
    
    # Also I need to close this new section before the existing </section> that closes the original wrapper.
    # The original wrapper was closed just before the <script> tags.
    # Let's replace the last </section> with </section>\n</section> (wait, no, I already closed the first one).
    # So the last </section> just closes the newly added <section class="w-full ...">.
    # That works perfectly! The original </section> will now act as the closer for the new slider section.
    
    new_content = parts[0] + parts[1]
    
    with open('reviews.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed slider width!")
else:
    print("Could not find slider marker.")
