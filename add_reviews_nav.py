import glob

html_files = glob.glob('*.html')

old_nav = """<a class="hover:text-ink transition-colors nav-link" href="blog.html">Blogs</a>"""
new_nav = """<a class="hover:text-ink transition-colors nav-link" href="blog.html">Blogs</a>
<a class="hover:text-ink transition-colors nav-link" href="reviews.html">Reviews</a>"""

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_nav in content:
        content = content.replace(old_nav, new_nav)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Added Reviews to nav in {count} files.")
