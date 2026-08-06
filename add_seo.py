import os
import glob
from bs4 import BeautifulSoup
import re

def prettify_name(filename):
    name = os.path.splitext(filename)[0]
    # Remove common prefixes and replace dashes/underscores
    name = name.replace('treatment-', '').replace('-', ' ').replace('_', ' ')
    name = name.title()
    if name.lower() == 'index':
        return "Home"
    return name

def add_seo_to_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    if not soup.head:
        return # Skip if no head
        
    filename = os.path.basename(filepath)
    page_name = prettify_name(filename)
    
    # 1. Update Title
    title_tag = soup.head.find('title')
    seo_title = f"{page_name} | Medshine Clinic - Advanced Skin & Hair Care in Mumbai"
    if page_name == "Home":
        seo_title = "Dr. Priya Jain | Best Skin Specialist & Aesthetic Physician in Mumbai | Medshine Clinic"
        
    if not title_tag:
        title_tag = soup.new_tag('title')
        soup.head.insert(0, title_tag)
    title_tag.string = seo_title
    
    # Remove existing SEO meta tags to prevent duplicates
    for meta in soup.head.find_all('meta', attrs={'name': ['description', 'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image']}):
        meta.decompose()
    for meta in soup.head.find_all('meta', attrs={'property': ['og:title', 'og:description', 'og:image', 'og:type', 'og:url']}):
        meta.decompose()

    # Define descriptions
    desc = f"Learn more about {page_name} at Medshine Clinic, Mumbai. Dr. Priya Jain offers advanced, evidence-based clinical cosmetology and aesthetic treatments."
    if page_name == "Home":
        desc = "Medshine Clinic in Mumbai by Dr. Priya Jain offers advanced laser rejuvenation, clinical acne scar revision, anti-aging contouring, and regenerative cellular therapies."
    elif page_name == "Results":
        desc = "View the real clinical results and before/after photos of advanced skin, hair, and laser treatments performed at Medshine Clinic by Dr. Priya Jain."
    elif page_name == "Treatments":
        desc = "Explore our wide range of aesthetic services including Laser Hair Reduction, Acne & Scar Treatments, Anti-Aging Injectables, and Regenerative Medicine."
        
    meta_tags_to_add = [
        {'name': 'description', 'content': desc},
        {'property': 'og:title', 'content': seo_title},
        {'property': 'og:description', 'content': desc},
        {'property': 'og:type', 'content': 'website'},
        {'property': 'og:image', 'content': 'https://medshineclinic.com/src/assets/dr_priya_portrait_pink.jpg'},
        {'name': 'twitter:card', 'content': 'summary_large_image'},
        {'name': 'twitter:title', 'content': seo_title},
        {'name': 'twitter:description', 'content': desc},
        {'name': 'twitter:image', 'content': 'https://medshineclinic.com/src/assets/dr_priya_portrait_pink.jpg'}
    ]
    
    # Insert new meta tags after <head> or charset
    for meta_attrs in reversed(meta_tags_to_add):
        new_meta = soup.new_tag('meta')
        new_meta.attrs.update(meta_attrs)
        title_tag.insert_after(new_meta)
        title_tag.insert_after("\n")
        
    # 2. Add Alt tags to Images
    for img in soup.find_all('img'):
        if not img.get('alt') or img.get('alt').strip() == "":
            src = img.get('src', '')
            if src:
                base_img = os.path.basename(src)
                alt_text = prettify_name(base_img)
                if not alt_text: alt_text = "Medshine Clinic Image"
                img['alt'] = alt_text
                
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
def process_all_files(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    for f in html_files:
        try:
            add_seo_to_file(f)
            print(f"Optimized: {os.path.basename(f)}")
        except Exception as e:
            print(f"Failed {f}: {e}")

if __name__ == "__main__":
    process_all_files('.')
