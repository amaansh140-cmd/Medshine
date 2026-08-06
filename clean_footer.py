import os
import glob

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update footer top margin
    content = content.replace(
        '<footer class="bg-ink/5 border-t border-ink/10 text-ink relative overflow-hidden mt-20">',
        '<footer class="bg-ink/5 border-t border-ink/10 text-ink relative overflow-hidden mt-12 md:mt-20">'
    )
    
    # 2. Update inner container padding
    content = content.replace(
        '<div class="max-w-[1240px] mx-auto px-6 md:px-10 pt-24 pb-10">',
        '<div class="max-w-[1240px] mx-auto px-6 md:px-10 pt-12 md:pt-24 pb-8 md:pb-10">'
    )
    
    # 3. Update grid gap and margin
    content = content.replace(
        '<div class="grid grid-cols-1 md:grid-cols-12 gap-12 md:gap-8 mb-16 relative z-10 stagger-group">',
        '<div class="grid grid-cols-1 md:grid-cols-12 gap-8 md:gap-8 mb-10 md:mb-16 relative z-10 stagger-group">'
    )
    
    # Also catch cases where stagger-group might be missing
    content = content.replace(
        '<div class="grid grid-cols-1 md:grid-cols-12 gap-12 md:gap-8 mb-16 relative z-10">',
        '<div class="grid grid-cols-1 md:grid-cols-12 gap-8 md:gap-8 mb-10 md:mb-16 relative z-10">'
    )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Updated footer classes across all HTML files.")
