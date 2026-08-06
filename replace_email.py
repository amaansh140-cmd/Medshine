import glob

html_files = glob.glob('*.html')
js_files = glob.glob('src/**/*.js', recursive=True)

all_files = html_files + js_files

old_email = "info@medshineclinic.com"
new_email = "contact@medshineclinic.com"

count = 0
for file_path in all_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_email in content:
        content = content.replace(old_email, new_email)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Updated email in {count} files.")
