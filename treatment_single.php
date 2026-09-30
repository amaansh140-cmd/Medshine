<?php
require 'api/config.php';
$stmt = $pdo->prepare("SELECT section_key, content_value FROM page_content WHERE page_slug = 'global'");
$stmt->execute();
$content = [];
while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
    $content[$row['section_key']] = $row['content_value'];
}

$slug = $_GET['slug'] ?? '';
$category = $_GET['cat'] ?? '';

$stmt = $pdo->prepare("SELECT * FROM treatments WHERE slug = ?");
$stmt->execute([$slug]);
$treatment = $stmt->fetch(PDO::FETCH_ASSOC);

if (!$treatment) {
    die("Treatment not found.");
}
?>
<!DOCTYPE html>
<html class="scroll-smooth" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title><?= htmlspecialchars($treatment['title']) ?> | Medshine Clinic</title>
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
      . { opacity: 0; transform: translateY(20px); transition: all 0.8s ease-out; }
      ..active { opacity: 1; transform: translateY(0); }
      .hover-scale { transition: transform 0.3s ease; }
      .hover-scale:hover { transform: scale(1.02); }
    </style>
    <link rel="stylesheet" crossorigin href="assets/style-wwR6AwHa.css">
</head>
<body class="bg-cream font-sans text-ink selection:bg-ink selection:text-cream overflow-x-hidden pt-28">

<nav class="fixed top-0 left-0 right-0 z-50 bg-cream/90 backdrop-blur-md border-b border-ink/5" id="navbar">
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
    <div class="flex items-center gap-2 text-sm font-medium text-inkmute mb-8  ">
        <a class="hover:text-ink transition-colors" href="index.php">Home</a>
        <svg fill="currentColor" height="14" viewbox="0 0 256 256" width="14" xmlns="http://www.w3.org/2000/svg"><path d="M181.66,133.66l-80,80a8,8,0,0,1-11.32-11.32L164.69,128,90.34,53.66a8,8,0,0,1,11.32-11.32l80,80A8,8,0,0,1,181.66,133.66Z"></path></svg>
        <a class="hover:text-ink transition-colors" href="treatments.php">Treatments</a>
        <svg fill="currentColor" height="14" viewbox="0 0 256 256" width="14" xmlns="http://www.w3.org/2000/svg"><path d="M181.66,133.66l-80,80a8,8,0,0,1-11.32-11.32L164.69,128,90.34,53.66a8,8,0,0,1,11.32-11.32l80,80A8,8,0,0,1,181.66,133.66Z"></path></svg>
        <a class="hover:text-ink transition-colors capitalize" href="treatment_category.php?cat=<?= urlencode($treatment['category']) ?>"><?= htmlspecialchars($treatment['category']) ?></a>
        <svg fill="currentColor" height="14" viewbox="0 0 256 256" width="14" xmlns="http://www.w3.org/2000/svg"><path d="M181.66,133.66l-80,80a8,8,0,0,1-11.32-11.32L164.69,128,90.34,53.66a8,8,0,0,1,11.32-11.32l80,80A8,8,0,0,1,181.66,133.66Z"></path></svg>
        <span class="text-ink"><?= htmlspecialchars($treatment['title']) ?></span>
    </div>

    <div class="max-w-[800px]">
        <h1 class="font-serif font-medium leading-[0.95] tracking-tight text-ink mb-10  " style="font-size: clamp(2.4rem, 5vw, 4.2rem);">
            <?= htmlspecialchars($treatment['title']) ?>
        </h1>
        
        <?php if($treatment['image']): ?>
        <div class="aspect-video w-full rounded-[24px] border border-ink/10 mb-12 flex items-center justify-center  overflow-hidden">
            <img alt="<?= htmlspecialchars($treatment['title']) ?>" class="w-full h-full object-cover " src="<?= htmlspecialchars(preg_replace('/-[a-zA-Z0-9_-]+\.(jpg|jpeg|png)$/i', '.$1', $treatment['image'])) ?>"/>
        </div>
        <?php endif; ?>
        
        <p class="text-[17px] md:text-[19px] text-inkmute leading-relaxed font-light ">
            <?= nl2br(htmlspecialchars($treatment['description'])) ?>
        </p>
        
        <div class="mt-10 ">
            <a class="inline-flex items-center justify-center bg-ink text-cream px-8 py-4 rounded-full font-medium hover:bg-black transition-colors hover-scale" href="contact.html">
              Book Appointment
            </a>
        </div>
    </div>
</main>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const reveals = document.querySelectorAll('.');
    reveals.forEach((el, index) => {
        setTimeout(() => {
            el.classList.add('active');
        }, index * 100);
    });
});
</script>
</body>
</html>
