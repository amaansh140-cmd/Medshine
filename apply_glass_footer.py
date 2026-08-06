import os
import shutil

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        old_class = '<footer class="bg-ink text-cream relative overflow-hidden mt-20">'
        new_class = '<footer class="bg-ink/85 backdrop-blur-2xl border border-cream/20 shadow-2xl text-cream relative overflow-hidden mt-16 mx-4 md:mx-10 mb-4 md:mb-8 rounded-[32px]">'
        
        if old_class in content:
            content = content.replace(old_class, new_class)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
                
            if os.path.exists(f'../Medshine/{filename}'):
                shutil.copy(filename, f'../Medshine/{filename}')

print("Glassmorphism applied to footer successfully.")
