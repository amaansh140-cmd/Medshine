import re

with open("reviews.html", "r", encoding="utf-8") as f:
    reviews_content = f.read()

with open("results.html", "r", encoding="utf-8") as f:
    results_content = f.read()

# Remove the broken block from results.html
broken_start = results_content.find('<!-- Patient Reviews Section -->')
broken_end = results_content.find('<script src="/src/main.js" type="module"></script>')
if broken_start != -1 and broken_end != -1:
    results_content = results_content[:broken_start] + results_content[broken_end:]
else:
    print("Could not find broken block to remove.")

# Extract the header and slider section from reviews.html
# The header section
start_header = reviews_content.find('<div class="flex flex-col items-center text-center mb-16 reveal-anim">')
end_header = reviews_content.find('</section>', start_header)
header_html = reviews_content[start_header:end_header]

# The slider section
start_slider = reviews_content.find('<!-- Slider Section -->')
end_slider = reviews_content.find('</section>', start_slider) + len('</section>')
slider_html = reviews_content[start_slider:end_slider]

# Construct the full block to insert
insert_html = f"""
<!-- Patient Reviews Section -->
<section class="max-w-[1240px] mx-auto px-6 md:px-10 pt-20 pb-8 border-t border-ink/10 mt-20">
{header_html}
</section>

{slider_html}
"""

# Insert before <script src="/src/main.js" type="module"></script>
target = '<script src="/src/main.js" type="module"></script>'
new_results_content = results_content.replace(target, insert_html + "\n" + target)

with open("results.html", "w", encoding="utf-8") as f:
    f.write(new_results_content)

print("Successfully fixed and appended full reviews section to results.html")
