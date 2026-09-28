<?php
header('Cache-Control: no-store, no-cache, must-revalidate, max-age=0');
header('Cache-Control: post-check=0, pre-check=0', false);
header('Pragma: no-cache');
require 'api/config.php';
$stmt = $pdo->prepare("SELECT section_key, content_value FROM page_content WHERE page_slug = 'global'");
$stmt->execute();
$content = [];
while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
    $content[$row['section_key']] = $row['content_value'];
}

$category = $_GET['cat'] ?? 'hair';

$stmt = $pdo->prepare("SELECT * FROM treatments WHERE category = ? ORDER BY title ASC");
$stmt->execute([$category]);
$treatments = $stmt->fetchAll(PDO::FETCH_ASSOC);

$titles = [
    'hair' => 'Hair Treatments',
    'skin' => 'Skin Treatments',
    'laser' => 'Laser Treatments',
    'medical' => 'Medical Treatments',
    'injectables' => 'Injectables',
    'non-surgical' => 'Non-Surgical',
    'regenerative' => 'Regenerative',
    'bridal' => 'Bridal'
];

$title = $titles[$category] ?? ucfirst($category) . ' Treatments';
?>
<!DOCTYPE html>
<html class="scroll-smooth" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title><?= htmlspecialchars($title) ?> | Medshine Clinic</title>
    <link href="https://fonts.googleapis.com" rel="preconnect"/>
    <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&amp;family=Inter:wght@300;400;500;600&amp;display=swap" rel="stylesheet"/>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            colors: {
              cream: '<?php echo $content["color_bg"] ?? "#FDFBF7"; ?>',
              creamdeep: '<?php echo $content["color_bg"] ?? "#F5F2EA"; ?>',
              ink: '<?php echo $content["color_text"] ?? "#065F46"; ?>',
              inkmute: '<?php echo $content["color_text"] ?? "#059669"; ?>',
              magenta: '<?php echo $content["color_accent"] ?? "#E11D48"; ?>', 
              magentadeep: '<?php echo $content["color_accent"] ?? "#E11D48"; ?>',
            },
            fontFamily: {
              sans: ['Inter', 'sans-serif'],
              serif: ['"Playfair Display"', 'serif'],
            }
          }
        }
      }
    </script>
    <style>
      .reveal-anim { opacity: 0; transform: translateY(20px); transition: all 0.8s ease-out; }
      .reveal-anim.active { opacity: 1; transform: translateY(0); }
      .hover-scale { transition: transform 0.3s ease; }
      .hover-scale:hover { transform: scale(1.02); }
      .whatsapp-float { position: fixed; bottom: 30px; left: 30px; background-color: #25D366; color: white; border-radius: 50%; padding: 16px; box-shadow: 0 10px 30px rgba(37, 211, 102, 0.4); z-index: 100; transition: transform 0.3s ease; display: flex; align-items: center; justify-content: center; }
      .whatsapp-float:hover { transform: translateY(-5px); box-shadow: 0 15px 35px rgba(37, 211, 102, 0.5); }
    </style>
    <!-- Use correct hashed stylesheet -->
    <link rel="stylesheet" crossorigin href="assets/style-wwR6AwHa.css">
</head>
<body class="bg-cream font-sans text-ink selection:bg-ink selection:text-cream overflow-x-hidden pt-28">

<nav class="fixed top-0 left-0 right-0 z-50 bg-cream/90 backdrop-blur-md border-b border-ink/5 transition-all duration-300" id="navbar">
    <div class="max-w-[1240px] mx-auto px-6 md:px-10 h-24 flex items-center justify-between">
        <a class="flex items-center gap-3 z-50 group hover-scale" href="index.php">
            <div class="w-10 h-10 rounded-full bg-ink flex items-center justify-center text-cream transition-transform duration-500 group-hover:rotate-180">
                <svg fill="currentColor" height="20" viewbox="0 0 256 256" width="20" xmlns="http://www.w3.org/2000/svg"><path d="M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24Zm43.81,68.19-28.28,66a8,8,0,0,1-3.72,3.72l-66,28.28a8,8,0,0,1-10.36-10.36l28.28-66a8,8,0,0,1,3.72-3.72l66-28.28A8,8,0,0,1,171.81,92.19ZM128,112a16,16,0,1,0,16,16A16,16,0,0,0,128,112Z"></path></svg>
            </div>
            <span class="font-serif font-semibold tracking-tight text-2xl">Medshine</span>
        </a>
        <div class="hidden md:flex items-center gap-8 text-sm font-medium">
            <a class="hover:text-ink/60 transition-colors" href="team.php">Team</a>
            <a class="hover:text-ink/60 transition-colors" href="treatments.php">Treatments</a>
            <a class="hover:text-ink/60 transition-colors" href="blog.html">Blogs</a>
            <a class="hover:text-ink/60 transition-colors" href="results.html">Results</a>
            <a class="hover:text-ink/60 transition-colors" href="contact.html">Contact</a>
        </div>
    </div>
</nav>

<main class="max-w-[1240px] mx-auto px-6 md:px-10 pb-20 md:pb-32">
    <div class="flex items-center gap-2 text-sm font-medium text-inkmute mb-8 reveal-anim reveal-fade">
        <a class="hover:text-ink transition-colors" href="index.php">Home</a>
        <svg fill="currentColor" height="14" viewbox="0 0 256 256" width="14" xmlns="http://www.w3.org/2000/svg"><path d="M181.66,133.66l-80,80a8,8,0,0,1-11.32-11.32L164.69,128,90.34,53.66a8,8,0,0,1,11.32-11.32l80,80A8,8,0,0,1,181.66,133.66Z"></path></svg>
        <a class="hover:text-ink transition-colors" href="treatments.php">Treatments</a>
        <svg fill="currentColor" height="14" viewbox="0 0 256 256" width="14" xmlns="http://www.w3.org/2000/svg"><path d="M181.66,133.66l-80,80a8,8,0,0,1-11.32-11.32L164.69,128,90.34,53.66a8,8,0,0,1,11.32-11.32l80,80A8,8,0,0,1,181.66,133.66Z"></path></svg>
        <span class="text-ink"><?= htmlspecialchars($title) ?></span>
    </div>

    <h1 class="font-serif font-medium leading-[0.95] tracking-tight text-ink mb-16 reveal-anim reveal-fade" style="font-size: clamp(2.7rem, 6vw, 5rem);">
        <?= htmlspecialchars($title) ?>
    </h1>

    <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6 grid-flow-dense auto-rows-[220px] md:auto-rows-[160px] stagger-group">
        <?php foreach($treatments as $index => $t): ?>
            <?php 
                $col_span = ($index % 4 == 0) ? 'md:col-span-2 lg:col-span-2' : 'md:col-span-1 lg:col-span-1';
                $row_span = ($index % 5 == 0) ? 'md:row-span-2 lg:row-span-2' : 'md:row-span-1 lg:row-span-1';
            ?>
            <a class="<?= $col_span ?> <?= $row_span ?> border border-ink/10 p-6 md:p-8 rounded-[24px] flex flex-col items-center justify-center text-center reveal-anim bg-white/5 relative overflow-hidden group hover-scale" 
               href="treatment_single.php?cat=<?= urlencode($category) ?>&slug=<?= urlencode($t['slug']) ?>">
                <span class="text-ink font-serif font-medium text-2xl md:text-3xl leading-snug"><?= htmlspecialchars($t['title']) ?></span>
            </a>
        <?php endforeach; ?>
    </div>
</main>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const reveals = document.querySelectorAll('.reveal-anim');
    reveals.forEach((el, index) => {
        setTimeout(() => {
            el.classList.add('active');
        }, index * 100);
    });
});
</script>
</body>
</html>
