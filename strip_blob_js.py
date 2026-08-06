import re
import shutil

with open('src/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# We can remove the blob mask logic which runs from the top of the file up to the end of animate() function
# The end of the animate function is probably around line 127.
# Let's use a regex to strip everything up to the line where Mobile Menu Setup begins.

parts = js.split("// Mobile Menu Setup")
if len(parts) > 1:
    new_js = "// Mobile Menu Setup\n" + parts[1]
    with open('src/main.js', 'w', encoding='utf-8') as f:
        f.write(new_js)
    shutil.copy('src/main.js', '../Medshine/src/main.js')

