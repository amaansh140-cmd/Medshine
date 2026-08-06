import re

with open("results.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('object-position: 50% 60%;', 'object-position: 50% 30%;')
content = content.replace('object-position: 50% 40%;', 'object-position: 50% 75%;')

with open("results.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Adjusted object-position to the correct direction.")
