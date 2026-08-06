import os
import shutil
import re

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove "Home" menu link globally
        home_link_pattern = r'<a href="index\.html" class="hover:text-ink transition-colors">Home</a>\s*'
        content = re.sub(home_link_pattern, '', content)
        
        # Remove "Back to Doctors" breadcrumb (only exists in index, dr-priya, dr-ankur)
        if filename in ['index.html', 'dr-priya.html', 'dr-ankur.html']:
            breadcrumb_pattern = r'<div class="flex items-center gap-4 mb-8">\s*<a href="[^"]+" class="text-inkmute hover:text-ink uppercase text-xs tracking-\[0\.28em\] font-semibold transition-colors">← Back to Doctors</a>\s*<div class="flex-1 h-px bg-ink/15"></div>\s*<span class="text-inkmute text-sm">[^<]+</span>\s*</div>'
            content = re.sub(breadcrumb_pattern, '', content)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        shutil.copy(filename, f'../Medshine/{filename}')

