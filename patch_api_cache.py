import glob

files = glob.glob('update_package/api/*.php')
for file in files:
    with open(file, 'r') as f:
        content = f.read()
        
    if 'header("Cache-Control:' not in content and 'header(\'Cache-Control:' not in content:
        # Some api files might start with <?php\nheader('Content-Type...
        # So replace <?php
        content = content.replace("<?php", "<?php\nheader('Cache-Control: no-store, no-cache, must-revalidate, max-age=0');\nheader('Cache-Control: post-check=0, pre-check=0', false);\nheader('Pragma: no-cache');")
        
        with open(file, 'w') as f:
            f.write(content)
