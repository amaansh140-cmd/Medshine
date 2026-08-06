import re

with open("results.html", "r", encoding="utf-8") as f:
    content = f.read()

# I need to find the two img tags in the first result and add object-position.
# Currently they are:
# <img src="/src/assets/after_1.jpg" alt="After Treatment" class="absolute inset-0 w-full h-full object-cover" />
# <img src="/src/assets/before_1.jpg" alt="Before Treatment" class="absolute inset-0 w-full h-full object-cover [clip-path:polygon(0_0,var(--split,50%)_0,var(--split,50%)_100%,0_100%)]" id="ba-image-1" />

after_img = '<img src="/src/assets/after_1.jpg" alt="After Treatment" class="absolute inset-0 w-full h-full object-cover"'
new_after_img = '<img src="/src/assets/after_1.jpg" alt="After Treatment" class="absolute inset-0 w-full h-full object-cover" style="object-position: 50% 60%;"'

before_img = '<img src="/src/assets/before_1.jpg" alt="Before Treatment" class="absolute inset-0 w-full h-full object-cover [clip-path:polygon(0_0,var(--split,50%)_0,var(--split,50%)_100%,0_100%)]" id="ba-image-1"'
new_before_img = '<img src="/src/assets/before_1.jpg" alt="Before Treatment" class="absolute inset-0 w-full h-full object-cover [clip-path:polygon(0_0,var(--split,50%)_0,var(--split,50%)_100%,0_100%)]" id="ba-image-1" style="object-position: 50% 40%;"'

content = content.replace(after_img, new_after_img)
content = content.replace(before_img, new_before_img)

with open("results.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Added object-position to fix alignment.")
