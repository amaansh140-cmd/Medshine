with open("results.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the after_1 image class
old_after_1 = '<img src="/src/assets/after_1.jpg" alt="After Treatment" class="absolute inset-0 w-full h-full object-cover" />'
new_after_1 = '<img src="/src/assets/after_1.jpg" alt="After Treatment" class="absolute inset-0 w-full h-full object-cover" style="object-position: center 75%;" />'

# Replace the before_1 image class
old_before_1 = '<img src="/src/assets/before_1.jpg" alt="Before Treatment" class="absolute inset-0 w-full h-full object-cover [clip-path:polygon(0_0,var(--split,50%)_0,var(--split,50%)_100%,0_100%)]" id="ba-image-1" />'
new_before_1 = '<img src="/src/assets/before_1.jpg" alt="Before Treatment" class="absolute inset-0 w-full h-full object-cover [clip-path:polygon(0_0,var(--split,50%)_0,var(--split,50%)_100%,0_100%)]" style="object-position: center 30%;" id="ba-image-1" />'

content = content.replace(old_after_1, new_after_1)
content = content.replace(old_before_1, new_before_1)

with open("results.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Aligned faces via CSS object-position!")
