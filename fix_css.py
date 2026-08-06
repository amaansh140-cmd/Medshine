import re
import shutil

with open('src/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# We can safely just remove these blocks or let them sit as unused. It's better to remove them.
# The user wants cream and emerald green. The ink variable in tailwind was changed, but are there hardcoded colors in CSS?

# Check for #1a1a1a or #10b981 in style.css
css = css.replace('#1a1a1a', '#065F46')
css = css.replace('#10b981', '#065F46')

with open('src/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

shutil.copy('src/style.css', '../Medshine/src/style.css')
