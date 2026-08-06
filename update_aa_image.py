import os

aa_file = 'treatment-skin-anti-ageing-treatments.html'

if os.path.exists(aa_file):
    with open(aa_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We swapped it previously, so the current image is treatment_medicated_facial_indian.jpeg
    content = content.replace('treatment_medicated_facial_indian.jpeg', 'treatment_anti_aging_new.jpeg')
    
    with open(aa_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated image for Anti-Aging.")
