import re

files = ['index.php', 'team.php', 'treatments.php']

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # Replace colors
    content = re.sub(r"cream: '#FDFBF7'", "cream: '<?php echo $content[\"color_bg\"] ?? \"#FDFBF7\"; ?>'", content)
    content = re.sub(r"creamdeep: '#F5F2EA'", "creamdeep: '<?php echo $content[\"color_bg\"] ?? \"#F5F2EA\"; ?>'", content)
    content = re.sub(r"ink: '#065F46'", "ink: '<?php echo $content[\"color_text\"] ?? \"#065F46\"; ?>'", content)
    content = re.sub(r"inkmute: '#059669'", "inkmute: '<?php echo $content[\"color_text\"] ?? \"#059669\"; ?>'", content)
    content = re.sub(r"magenta: '#111111'", "magenta: '<?php echo $content[\"color_accent\"] ?? \"#E11D48\"; ?>'", content)
    content = re.sub(r"magentadeep: '#000000'", "magentadeep: '<?php echo $content[\"color_accent\"] ?? \"#E11D48\"; ?>'", content)
    
    # If treatments.php doesn't have magenta, add it
    if 'magenta:' not in content and 'colors: {' in content:
        content = content.replace('colors: {', 'colors: {\n              magenta: \'<?php echo $content["color_accent"] ?? "#E11D48"; ?>\',')

    # Replace Index specific variables
    if file == 'index.php':
        content = re.sub(r"Dr\. Priya <em class=\"[^\"]+\">Jain<\/em>", "<?php echo $content['hero_title'] ?? 'Dr. Priya <em class=\"font-light italic text-inkmute\">Jain</em>'; ?>", content)
        content = re.sub(r'\"We do not treat skin as a canvas[^<]+', "<?php echo nl2br($content['hero_subtitle'] ?? '\"We do not treat skin as a canvas for cosmetic trends. We treat it as a vital biological organ that flourishes under precision diagnosis and empathetic medical care.\"'); ?>", content)
        content = re.sub(r'As the visionary founder[^<]+', "<?php echo nl2br($content['about_text'] ?? 'As the visionary founder of Medshine Clinic, Dr. Priya Jain (MBBS, FFAC Fellowships) has dedicated over 15 years to advancing clinical cosmetology and aesthetic services. As a renowned Skin Specialist and Aesthetic Physician, her evidence-based philosophy emphasizes cellular skin health, precision diagnostics, and tailored non-invasive rejuvenation.'); ?>", content)

    # Replace Team specific variables
    if file == 'team.php':
        content = re.sub(r'Our Dedicated <em class=\"[^\"]+\">Team<\/em>', "<?php echo $content['page_title'] ?? 'Our Dedicated <em class=\"font-light italic text-inkmute\">Team</em>'; ?>", content)

    # Replace Treatments specific variables
    if file == 'treatments.php':
        content = re.sub(r'Specialized Treatments', "<?php echo $content['page_title'] ?? 'Specialized Treatments'; ?>", content)

    with open(file, 'w') as f:
        f.write(content)

print("Done replacing.")
