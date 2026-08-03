import re
import glob

category_files = [
    "treatment-skin.html", "treatment-medical.html", "treatment-hair.html", 
    "treatment-laser.html", "treatment-injectables.html", "treatment-non-surgical.html", 
    "treatment-bridal.html", "treatments.html"
]

all_html = glob.glob("treatment-*.html")
detail_pages = [f for f in all_html if f not in category_files]

base_layer_btn = """
          <div class="mt-10 reveal-anim">
            <a href="contact.html" class="inline-flex items-center justify-center bg-ink text-cream px-8 py-4 rounded-full font-medium hover:bg-black transition-colors hover-scale">
              Book Appointment
            </a>
          </div>
"""

reveal_layer_btn = """
          <div class="mt-10 reveal-anim">
            <a href="contact.html" class="inline-flex items-center justify-center bg-cream text-ink px-8 py-4 rounded-full font-medium hover:bg-white transition-colors hover-scale">
              Book Appointment
            </a>
          </div>
"""

for filepath in detail_pages:
    with open(filepath, 'r') as f:
        content = f.read()

    # Base layer: <p ... text-inkmute ...> ... </p>
    p_inkmute_pattern = r'(<p class="text-\[17px\] md:text-\[19px\] text-inkmute leading-relaxed font-light reveal-anim">.*?</p>)'
    
    # Check if we already have the button to avoid duplication
    if 'Book Appointment' not in content:
        # We need to replace the first occurrence (base layer) and the second occurrence (reveal layer) separately
        # But wait, we can just replace them using re.sub with a count if they were identical, but they are not.
        
        # Base layer replacement
        content = re.sub(p_inkmute_pattern, rf'\1{base_layer_btn}', content, count=1, flags=re.DOTALL)
        
        # Reveal layer replacement
        p_cream_pattern = r'(<p class="text-\[17px\] md:text-\[19px\] text-cream/70 leading-relaxed font-light reveal-anim">.*?</p>)'
        content = re.sub(p_cream_pattern, rf'\1{reveal_layer_btn}', content, count=1, flags=re.DOTALL)

        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Added buttons to {filepath}")
    else:
        print(f"Buttons already exist in {filepath}")

print("Done adding buttons!")
