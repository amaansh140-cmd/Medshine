import glob

html_files = glob.glob('*.html')

old_text = """<a class="hover:text-ink transition-colors" href="mailto:contact@medshineclinic.com">contact@medshineclinic.com</a>
</li>
</ul>"""

new_text = """<a class="hover:text-ink transition-colors" href="mailto:contact@medshineclinic.com">contact@medshineclinic.com</a>
</li>
<li class="flex gap-3 items-start">
<svg class="flex-shrink-0 text-ink mt-0.5" fill="currentColor" height="16" viewbox="0 0 256 256" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24Zm0,192a88,88,0,1,1,88-88A88.1,88.1,0,0,1,128,216Zm64-88a8,8,0,0,1-8,8H128a8,8,0,0,1-8-8V72a8,8,0,0,1,16,0v48h48A8,8,0,0,1,192,128Z"></path></svg>
<div>
  12-9 PM (Mon-Sat)<br>
  <span class="text-xs opacity-75">Sun by appointment</span>
</div>
</li>
</ul>"""

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Added timings to {count} files.")
