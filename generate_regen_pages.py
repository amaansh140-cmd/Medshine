import re
import os
import shutil

treatments = [
    {
        "title": "PRP (Platelet-Rich Plasma)",
        "file": "treatment-regenerative-prp.html",
        "desc": "Uses your own blood platelets, which release growth factors that support healing and tissue repair."
    },
    {
        "title": "PRF (Platelet-Rich Fibrin)",
        "file": "treatment-regenerative-prf.html",
        "desc": "A newer platelet concentrate that releases growth factors more gradually than PRP."
    },
    {
        "title": "Exosome therapy",
        "file": "treatment-regenerative-exosome.html",
        "desc": "Uses extracellular vesicles that contain signaling molecules which may help with tissue repair and regeneration. Clinical research is ongoing, and regulatory approval varies by country."
    },
    {
        "title": "Regenera Activa",
        "file": "treatment-regenerative-regenera-activa.html",
        "desc": "Uses a small sample of your own scalp tissue to produce a suspension containing progenitor cells and growth factors for hair restoration."
    },
    {
        "title": "Autologous fat grafting (nanofat/microfat)",
        "file": "treatment-regenerative-autologous-fat.html",
        "desc": "Uses the patient's own fat, which contains regenerative cells and growth factors, for selected reconstructive and aesthetic indications."
    },
    {
        "title": "Stem cell-based therapies",
        "file": "treatment-regenerative-stem-cell.html",
        "desc": "These are an active area of research. Many marketed cosmetic \"stem cell\" treatments are not supported by strong clinical evidence, and true stem cell therapies are regulated differently in many countries."
    }
]

with open('treatment-medical-diabetes-mellitus.html', 'r') as f:
    template = f.read()

# Modify the template to remove the image block
template = re.sub(r'<div class="aspect-video w-full rounded-\[24px\].*?</div>', '', template, flags=re.DOTALL)

for t in treatments:
    content = template
    # Replace Medical Treatments with Regenerative Medicines
    content = content.replace("Medical Treatments", "Regenerative Medicines")
    content = content.replace("treatment-medical.html", "treatment-regenerative.html")
    
    # Replace title
    content = re.sub(r'>\s*Diabetes Mellitus\s*</h1>', f'>\n            {t["title"]}\n          </h1>', content)
    
    # Replace paragraph (it's the only <p> in the template)
    content = re.sub(r'<p class="([^"]*)">\s*Manage your blood sugar effectively with comprehensive Medshine diabetes care\. The Medshine medical team focuses on lifestyle integration and precision medicine to prevent complications and keep you thriving\.\s*</p>', 
                     f'<p class="\\1">\n            {t["desc"]}\n          </p>', content)
    
    with open(t["file"], 'w') as f:
        f.write(content)
    
    # Copy to Medshine
    shutil.copy(t["file"], f'../Medshine/{t["file"]}')

# Now we need to update treatment-regenerative.html to use <a> tags instead of <div> tags for the grid
with open('treatment-regenerative.html', 'r') as f:
    regen_content = f.read()

for t in treatments:
    # Find the div for this treatment
    escaped_title = re.escape(t["title"])
    # For Base Layer
    regen_content = re.sub(
        r'<div class="(md:col-span-2[^"]*)">\s*<span class="([^"]*)">' + escaped_title + r'</span>\s*<p class="([^"]*)">.*?</p>\s*</div>',
        f'<a href="{t["file"]}" class="\\1">\n              <span class="\\2">{t["title"]}</span>\n              <p class="\\3">{t["desc"]}</p>\n            </a>',
        regen_content, flags=re.DOTALL
    )

with open('treatment-regenerative.html', 'w') as f:
    f.write(regen_content)

shutil.copy('treatment-regenerative.html', '../Medshine/treatment-regenerative.html')

