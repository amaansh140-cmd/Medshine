import glob

html_files = glob.glob('*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace href="index.html" with href="/"
    new_content = content.replace('href="index.html"', 'href="/"')
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

print(f"Updated {len(html_files)} files.")
