import os

files = ['index.php']
replacements = {
    '/assets/clinic-room-DT-0E_O2.jpg': '/clinic-room.jpg',
    '/assets/product-shelf-BtkKn5Gz.jpg': '/product-shelf.jpg',
    '/assets/face-exam-DWbZtlmp.PNG': '/face-exam.PNG',
    '/assets/hair-treatment-swOo_HRQ.PNG': '/hair-treatment.PNG',
    '/assets/desk-consult-BXHCdwC3.PNG': '/desk-consult.PNG'
}

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(f, 'w') as file:
        file.write(content)
