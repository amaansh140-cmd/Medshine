import os

anti_aging_file = 'treatment-skin-anti-ageing-treatments.html'
med_facial_file = 'treatment-skin-medicated-facials.html'

if os.path.exists(anti_aging_file):
    with open(anti_aging_file, 'r', encoding='utf-8') as f:
        aa_content = f.read()
    aa_content = aa_content.replace('treatment_anti_aging_indian.jpeg', 'treatment_medicated_facial_indian.jpeg')
    with open(anti_aging_file, 'w', encoding='utf-8') as f:
        f.write(aa_content)

if os.path.exists(med_facial_file):
    with open(med_facial_file, 'r', encoding='utf-8') as f:
        mf_content = f.read()
    mf_content = mf_content.replace('treatment_medicated_facial_indian.jpeg', 'treatment_anti_aging_indian.jpeg')
    with open(med_facial_file, 'w', encoding='utf-8') as f:
        f.write(mf_content)

print("Swapped images!")
