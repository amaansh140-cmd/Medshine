import os
import shutil
from bs4 import BeautifulSoup

target_files = ['team.html', 'dr-priya.html', 'dr-ankur.html']

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')
        
        slider = soup.find('section', id='hero-slider-section')
        if slider:
            slider.decompose()

        # The script tag for smooth slider is inside a script tag right after the slider or inside the body. 
        # Since the javascript references 'hero-slider-section', we should also remove that script if it exists.
        for script in soup.find_all('script'):
            if script.string and 'smooth-slider-track' in script.string:
                script.decompose()
        
        new_content = str(soup)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        if os.path.exists(f'../Medshine/{filename}'):
            shutil.copy(filename, f'../Medshine/{filename}')
            
print("Slider removed from team pages!")
