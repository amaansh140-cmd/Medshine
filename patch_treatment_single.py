import re

with open('treatment_single.php', 'r') as f:
    content = f.read()

# Replace: src="<?= htmlspecialchars($treatment['image']) ?>"
# With: src="<?= htmlspecialchars(preg_replace('/-[a-zA-Z0-9_-]+\.(jpg|jpeg|png)$/i', '.$1', $treatment['image'])) ?>"

new_content = content.replace(
    'src="<?= htmlspecialchars($treatment[\'image\']) ?>"',
    'src="<?= htmlspecialchars(preg_replace(\'/-[a-zA-Z0-9_-]+\\.(jpg|jpeg|png)$/i\', \'.$1\', $treatment[\'image\'])) ?>"'
)

with open('treatment_single.php', 'w') as f:
    f.write(new_content)
print("treatment_single.php patched!")
