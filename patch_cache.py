import glob

files = glob.glob('update_package/*.php')
for file in files:
    with open(file, 'r') as f:
        content = f.read()
        
    if 'header("Cache-Control:' not in content:
        content = content.replace("<?php\nrequire 'api/config.php';", "<?php\nheader('Cache-Control: no-store, no-cache, must-revalidate, max-age=0');\nheader('Cache-Control: post-check=0, pre-check=0', false);\nheader('Pragma: no-cache');\nrequire 'api/config.php';")
        
        with open(file, 'w') as f:
            f.write(content)
