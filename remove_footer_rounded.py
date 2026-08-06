import os
import shutil

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove rounded corners
        # Old: class="bg-ink/5 border-t border-ink/10 text-ink relative overflow-hidden mt-20 rounded-t-[40px]"
        # New: class="bg-ink/5 border-t border-ink/10 text-ink relative overflow-hidden mt-20"
        
        old_classes = 'class="bg-ink/5 border-t border-ink/10 text-ink relative overflow-hidden mt-20 rounded-t-[40px]"'
        new_classes = 'class="bg-ink/5 border-t border-ink/10 text-ink relative overflow-hidden mt-20"'
        
        if old_classes in content:
            content = content.replace(old_classes, new_classes)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
                
            if os.path.exists(f'../Medshine/{filename}'):
                shutil.copy(filename, f'../Medshine/{filename}')

print("Footer rounded corners removed!")
