with open('treatment-regenerative.html', 'r') as f:
    content = f.read()

treatments = [
    ("PRP (Platelet-Rich Plasma)", "treatment-regenerative-prp.html"),
    ("PRF (Platelet-Rich Fibrin)", "treatment-regenerative-prf.html"),
    ("Exosome therapy", "treatment-regenerative-exosome.html"),
    ("Regenera Activa", "treatment-regenerative-regenera-activa.html"),
    ("Autologous fat grafting (nanofat/microfat)", "treatment-regenerative-autologous-fat.html"),
    ("Stem cell-based therapies", "treatment-regenerative-stem-cell.html")
]

for title, link in treatments:
    # We want to replace the opening <div ... group"> that precedes this title with <a href="link" ... group">
    # and the closing </div> with </a>
    
    # Split content around the title
    parts = content.split(title)
    if len(parts) >= 2:
        # For each occurrence of the title (base layer and reveal layer)
        for i in range(len(parts)-1):
            before = parts[i]
            after = parts[i+1]
            
            # Find the last <div class="md:col-span-2... in 'before'
            div_start = before.rfind('<div class="md:col-span-2')
            if div_start != -1:
                before = before[:div_start] + '<a href="' + link + '" class="' + before[div_start+12:]
            
            # Find the first </div> in 'after'
            div_end = after.find('</div>')
            if div_end != -1:
                after = after[:div_end] + '</a>' + after[div_end+6:]
                
            parts[i] = before
            parts[i+1] = after
        
        content = title.join(parts)

with open('treatment-regenerative.html', 'w') as f:
    f.write(content)

