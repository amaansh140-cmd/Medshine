import os
import shutil

target_files = ['index.html', 'dr-priya.html', 'dr-ankur.html']

unsplash_3 = 'https://images.unsplash.com/photo-1616394584738-fc6e612e71c9?q=80&w=600&auto=format&fit=crop'

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace(unsplash_3, '/public/product-shelf.jpg')
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
                
        if os.path.exists(f'../Medshine/{filename}'):
            shutil.copy(filename, f'../Medshine/{filename}')

print("Slider image 3 updated!")
