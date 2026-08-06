import os
import glob
import re

bottom_part = open('bottom_part.html', 'r').read()

files = glob.glob('treatment-*.html')
for f in files:
    if os.path.getsize(f) < 8000:
        with open(f, 'r') as file:
            content = file.read()
        
        # Remove </body></html> and any trailing whitespace
        content = re.sub(r'</body>\s*</html>\s*$', '', content)
        
        # Also remove just </body> or </html> if they are separate
        content = content.replace('</body>', '').replace('</html>', '').strip()
        
        # Append the bottom part
        new_content = content + '\n' + bottom_part
        
        with open(f, 'w') as file:
            file.write(new_content)
        
        print(f"Fixed {f}")
        
