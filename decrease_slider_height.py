import os
import shutil
import re

target_files = ['index.html', 'dr-priya.html', 'dr-ankur.html']

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace the height class. Currently it is: h-[360px] md:h-[480px]
        # Change to: h-[320px] md:h-[420px]
        if 'h-[360px] md:h-[480px]' in content:
            content = content.replace('h-[360px] md:h-[480px]', 'h-[320px] md:h-[420px]')
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
                
            if os.path.exists(f'../Medshine/{filename}'):
                shutil.copy(filename, f'../Medshine/{filename}')

print("Slider height decreased!")
