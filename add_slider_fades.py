import os
import shutil
import re

target_files = ['index.html', 'dr-priya.html', 'dr-ankur.html']

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the slider section
        search_str = '<section class="max-w-[100vw] overflow-hidden mb-28 py-6">'
        
        replacement = """<section class="max-w-[100vw] overflow-hidden mb-28 py-6 relative">
  <!-- Gradient Fades for edges -->
  <div class="absolute inset-y-0 left-0 w-12 md:w-32 bg-gradient-to-r from-[#FAF8F5] to-transparent z-10 pointer-events-none"></div>
  <div class="absolute inset-y-0 right-0 w-12 md:w-32 bg-gradient-to-l from-[#FAF8F5] to-transparent z-10 pointer-events-none"></div>"""

        if search_str in content:
            content = content.replace(search_str, replacement)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
                
            if os.path.exists(f'../Medshine/{filename}'):
                shutil.copy(filename, f'../Medshine/{filename}')

print("Slider edge fades added!")
