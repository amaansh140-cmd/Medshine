import glob

html_files = glob.glob('*.html')

old_text = """<li>• Fractional CO2 &amp; Erbium Resurfacing</li>
<li>• Q-Switched Melasma &amp; Pigment Reduction</li>
<li>• Vascular &amp; Redness Therapy</li>"""

new_text = """<li>• Q switch for laser toning</li>
<li>• Pico for Melasma</li>
<li>• Carbon for oily acne prone skin</li>"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated laser bullets.")
