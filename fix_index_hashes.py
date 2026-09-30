import re

with open('index.php', 'r') as f:
    content = f.read()

# Replace src="/assets/NAME-HASH.EXT" with src="/assets/NAME.EXT"
# Actually, laser-machine is in public, so it should be src="/laser-machine.jpg"
# Let's do it manually since there are only 3 images.

content = re.sub(r'src="/assets/dr_priya_portrait_pink-[a-zA-Z0-9_-]+\.jpg"', 'src="/assets/dr_priya_portrait_pink.jpg"', content)
content = re.sub(r'srcset="/assets/dr_priya_mobile_hero-[a-zA-Z0-9_-]+\.jpg"', 'srcset="/assets/dr_priya_mobile_hero.jpg"', content)
content = re.sub(r'src="/assets/laser-machine-[a-zA-Z0-9_-]+\.jpg"', 'src="/laser-machine.jpg"', content)

with open('index.php', 'w') as f:
    f.write(content)

print("index.php patched!")
