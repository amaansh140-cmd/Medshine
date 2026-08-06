import os
import shutil

target_files = ['index.html', 'dr-priya.html', 'dr-ankur.html']

unsplash_1 = 'https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?q=80&w=600&auto=format&fit=crop'
unsplash_2 = 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?q=80&w=600&auto=format&fit=crop'

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace(unsplash_1, '/public/clinic-room.jpg')
        content = content.replace(unsplash_2, '/public/laser-machine.jpg')
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
                
        if os.path.exists(f'../Medshine/{filename}'):
            shutil.copy(filename, f'../Medshine/{filename}')

print("Slider images updated!")
