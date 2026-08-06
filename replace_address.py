import glob

html_files = glob.glob('*.html')

old_address_footer = "<span>Medii Derma Shine, Shastri Nagar, Goregaon West, Mumbai, Maharashtra 400104</span>"
new_address_footer = "<span>Unit shop no 1 ground floor Sarvodya chs near Bangur Nagar metro station, Shastri nagar Road no 1 next to The Tree house School Goregaon West Mumbai Maharashtra 400104</span>"

old_address_contact = '<p class="reveal-anim">No. 8, SARVODYA CHS, Shastri Nagar Road No. 1,<br/>Azad Nagar, Goregaon West, Mumbai 400104</p>'
new_address_contact = '<p class="reveal-anim">Unit shop no 1 ground floor Sarvodya chs near Bangur Nagar metro station,<br/>Shastri nagar Road no 1 next to The Tree house School, Goregaon West, Mumbai Maharashtra 400104</p>'

count_footer = 0
count_contact = 0

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated = False
    
    if old_address_footer in content:
        content = content.replace(old_address_footer, new_address_footer)
        updated = True
        count_footer += 1
        
    if old_address_contact in content:
        content = content.replace(old_address_contact, new_address_contact)
        updated = True
        count_contact += 1
        
    if updated:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Updated footer address in {count_footer} files.")
print(f"Updated contact address in {count_contact} files.")
