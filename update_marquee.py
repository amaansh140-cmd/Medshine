import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Section Class
old_section = '<section class="w-full bg-[#0a0a0a] text-cream py-8 md:py-12 overflow-hidden relative z-10 border-y border-[#222]">'
new_section = '<section class="w-full bg-ink/5 backdrop-blur-md text-ink py-8 md:py-12 mb-20 md:mb-28 overflow-hidden relative z-10 border-y border-ink/10">'
content = content.replace(old_section, new_section)

# 2. Update text colors inside the marquee
# We need to find the marquee block and replace colors inside it
marquee_pattern = re.compile(r'(<!-- Achievements Marquee -->.*?)</section>', re.DOTALL)
match = marquee_pattern.search(content)

if match:
    marquee_content = match.group(0)
    
    # border-cream/15 -> border-ink/10
    marquee_content = marquee_content.replace('border-cream/15', 'border-ink/10')
    
    # text-cream/70 -> text-inkmute
    marquee_content = marquee_content.replace('text-cream/70', 'text-inkmute')
    
    # text-inkmute/90 -> text-magenta (or keep ink/magenta as is). The + was text-inkmute/90 which is fine on light background, 
    # but wait, let's just make sure it's readable. It was text-inkmute/90. Actually, text-inkmute/90 is dark green, which is fine! Wait, the original was text-inkmute/90? No, it was text-inkmute/90.
    
    content = content.replace(match.group(0), marquee_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated slider styles!")
