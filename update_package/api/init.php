<?php
header('Cache-Control: no-store, no-cache, must-revalidate, max-age=0');
header('Cache-Control: post-check=0, pre-check=0', false);
header('Pragma: no-cache');
require 'config.php';

try {
    // Create users table
    $pdo->exec("CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )");

    // Create blogs table
    $pdo->exec("CREATE TABLE IF NOT EXISTS blogs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        category VARCHAR(100),
        read_time VARCHAR(50),
        image VARCHAR(500),
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )");

    // Create pages table
    $pdo->exec("CREATE TABLE IF NOT EXISTS pages (
        slug VARCHAR(100) PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    )");

    // Create page_content table
    $pdo->exec("CREATE TABLE IF NOT EXISTS page_content (
        id INT AUTO_INCREMENT PRIMARY KEY,
        page_slug VARCHAR(100) NOT NULL,
        section_key VARCHAR(100) NOT NULL,
        label VARCHAR(255) NOT NULL,
        content_type VARCHAR(50) NOT NULL DEFAULT 'text',
        content_value TEXT,
        UNIQUE KEY page_key (page_slug, section_key),
        FOREIGN KEY (page_slug) REFERENCES pages(slug) ON DELETE CASCADE
    )");

    // Seed Pages
    $pdo->exec("INSERT IGNORE INTO pages (slug, name) VALUES ('index', 'Home Page')");
    $pdo->exec("INSERT IGNORE INTO pages (slug, name) VALUES ('team', 'Team Page')");
    $pdo->exec("INSERT IGNORE INTO pages (slug, name) VALUES ('treatments', 'Treatments Page')");
    $pdo->exec("INSERT IGNORE INTO pages (slug, name) VALUES ('global', 'Global Design (Colors)')");
    
    // Seed default content
    $insertContent = $pdo->prepare("INSERT IGNORE INTO page_content (page_slug, section_key, label, content_type, content_value) VALUES (?, ?, ?, ?, ?)");
    
    $defaults = [
        ['index', 'hero_title', 'Hero Title', 'text', 'Dr. Priya <em class="font-light italic text-inkmute">Jain</em>'],
        ['index', 'hero_subtitle', 'Hero Subtitle', 'textarea', '"We do not treat skin as a canvas for cosmetic trends. We treat it as a vital biological organ that flourishes under precision diagnosis and empathetic medical care."'],
        ['index', 'about_text', 'About Us Text', 'textarea', 'As the visionary founder of Medshine Clinic, Dr. Priya Jain (MBBS, FFAC Fellowships) has dedicated over 15 years to advancing clinical cosmetology and aesthetic services. As a renowned Skin Specialist and Aesthetic Physician, her evidence-based philosophy emphasizes cellular skin health, precision diagnostics, and tailored non-invasive rejuvenation.'],
        ['global', 'color_bg', 'Background Color (Cream)', 'text', '#FDFBF7'],
        ['global', 'color_text', 'Main Text Color (Dark Green)', 'text', '#065F46'],
        ['global', 'color_accent', 'Accent Color (Magenta/Pink)', 'text', '#E11D48'],
        ['team', 'page_title', 'Main Title', 'text', 'Our Team of Experts'],
        ['treatments', 'page_title', 'Main Title', 'text', 'Advanced Clinical Treatments'],
    ];

    foreach ($defaults as $row) {
        $insertContent->execute($row);
    }
    
    // Create treatments table
    $pdo->exec("CREATE TABLE IF NOT EXISTS treatments (
        id INT AUTO_INCREMENT PRIMARY KEY,
        category VARCHAR(100) NOT NULL,
        slug VARCHAR(255) UNIQUE NOT NULL,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        image VARCHAR(500),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )");
    
    
    $json = file_get_contents(__DIR__ . "/treatments.json");
    $treatmentsData = json_decode($json, true);
    if ($treatmentsData) {
        $stmtTreat = $pdo->prepare("INSERT IGNORE INTO treatments (category, slug, title, description, image) VALUES (?, ?, ?, ?, ?)");
        foreach ($treatmentsData as $t) {
            $stmtTreat->execute([$t['category'], $t['slug'], $t['title'], $t['description'], $t['image']]);
        }
    }

    
    // Check if admin user exists
    $stmt = $pdo->query("SELECT * FROM users");
    if ($stmt->rowCount() == 0) {
        $defaultPassword = password_hash('admin123', PASSWORD_DEFAULT);
        $insert = $pdo->prepare("INSERT INTO users (email, password) VALUES (?, ?)");
        $insert->execute(['admin@medshineclinic.com', $defaultPassword]);
    }

    echo "Database initialized successfully!";
} catch(PDOException $e) {
    echo "Error: " . $e->getMessage();
}
?>
