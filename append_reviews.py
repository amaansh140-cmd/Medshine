import re

with open("reviews.html", "r", encoding="utf-8") as f:
    reviews_content = f.read()

with open("results.html", "r", encoding="utf-8") as f:
    results_content = f.read()

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
if target in results_content:
    new_results_content = results_content.replace(target, insert_html + "\n" + target)
    with open("results.html", "w", encoding="utf-8") as f:
        f.write(new_results_content)
    print("Successfully appended reviews to results.html")
else:
    print("Could not find the target script tag to insert before.")
