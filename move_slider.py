import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the Marquee block
marquee_pattern = re.compile(r'(<!-- Achievements Marquee -->.*?</section>\n)', re.DOTALL)
match = marquee_pattern.search(content)

if match:
    marquee_block = match.group(1)
    
    # Remove from current location
    content = content.replace(marquee_block, '')
    
    # Insert before <!-- Specialties & Procedures -->
    target = '<!-- Specialties & Procedures -->'
    if target in content:
        content = content.replace(target, marquee_block + target)
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully moved the slider!")
    else:
        print("Could not find Specialties target.")
else:
    print("Could not find Marquee block.")

