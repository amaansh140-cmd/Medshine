from bs4 import BeautifulSoup
import shutil

with open('team.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Update title
title = soup.find('title')
if title:
    title.string = "Our Team | Medshine Clinic"

# Remove unwanted sections
for section_id in ['exist', 'proof', 'testimonials', 'values', 'join']:
    sec = soup.find('section', id=section_id)
    if sec:
        sec.decompose()

# The second section (the big picture strip with "A life restored...") can also be removed to make it a clean Team page
# It doesn't have an ID. Let's find it by looking for the h2 text "A life restored"
h2_life = soup.find(lambda tag: tag.name == "h2" and "A life restored" in tag.text)
if h2_life:
    parent_section = h2_life.find_parent('section')
    if parent_section:
        parent_section.decompose()

# Update the top Hero section
# The first section is the hero. Let's find the h1 and update it.
h1 = soup.find('h1')
if h1:
    h1.clear()
    h1.append("Our Dedicated ")
    em = soup.new_tag("em", attrs={"class": "font-light italic text-inkmute"})
    em.string = "Team"
    h1.append(em)

# Update the subtext in the hero
p = soup.find('p', text=lambda t: t and "At Medshine Clinic, we provide holistic" in t)
if p:
    p.string = "Meet the experienced medical professionals dedicated to your clinical health and aesthetic care."
    
# Change the "About Medshine Clinic" small text at the very top
span = soup.find('span', text="About Medshine Clinic")
if span:
    span.string = "Our Team"

with open('team.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

shutil.copy('team.html', '../Medshine/team.html')
