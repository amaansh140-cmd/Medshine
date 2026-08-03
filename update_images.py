import re
import glob

# Function to update subpages based on the main index page
def update_subpages(index_file):
    with open(index_file, 'r') as f:
        content = f.read()
    
    # Regex to find blocks like:
    # <a href="treatment-medical-diabetes-mellitus.html" ... style="background-image: url('/src/assets/treatment_diabetes_indian.jpeg'); ...">
    pattern = r'<a href="([^"]+)"[^>]+style="[^"]*background-image:\s*url\(\'([^\']+)\'\)[^"]*"[^>]*>'
    matches = re.findall(pattern, content)
    
    for href, img_url in matches:
        print(f"Updating {href} with image {img_url}")
        try:
            with open(href, 'r') as f:
                page_content = f.read()
            
            # Replace the img src inside the page
            # Assuming the img tag looks like <img src="/src/assets/..." alt="..." ...>
            page_content = re.sub(r'<img src="[^"]+"( alt="[^"]+" class="w-full h-full object-cover[^"]*")', rf'<img src="{img_url}"\1', page_content)
            
            with open(href, 'w') as f:
                f.write(page_content)
        except Exception as e:
            print(f"Error processing {href}: {e}")

update_subpages("treatment-skin.html")
update_subpages("treatment-medical.html")
update_subpages("treatment-hair.html")
update_subpages("treatment-laser.html")
update_subpages("treatment-injectables.html")
update_subpages("treatment-bridal.html")
update_subpages("treatment-non-surgical.html")
print("Done!")
