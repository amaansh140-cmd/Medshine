import os
import shutil

target_files = ['index.html', 'dr-priya.html', 'dr-ankur.html']

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace absolute /public/ paths with relative public/ paths
        content = content.replace('src="/public/', 'src="public/')
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
                
        if os.path.exists(f'../Medshine/{filename}'):
            shutil.copy(filename, f'../Medshine/{filename}')

print("Image paths fixed to be relative!")
