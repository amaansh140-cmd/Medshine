import glob
import re

html_files = glob.glob("*.html")

for filename in html_files:
    with open(filename, 'r') as f:
        content = f.read()
        
    if "auto-rows-auto md:auto-rows-[160px]" in content:
        # We replace auto-rows-auto with auto-rows-[200px] or min-h-[200px] for mobile
        new_content = content.replace("auto-rows-auto md:auto-rows-[160px]", "auto-rows-[220px] md:auto-rows-[160px]")
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Fixed grid in {filename}")
