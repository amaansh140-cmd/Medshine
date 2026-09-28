<?php
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
    $stmt = $pdo->query("SELECT * FROM pages");
    if ($stmt->rowCount() == 0) {
        $pdo->exec("INSERT INTO pages (slug, name) VALUES ('index', 'Home Page')");
        $pdo->exec("INSERT INTO pages (slug, name) VALUES ('team', 'Team Page')");
        $pdo->exec("INSERT INTO pages (slug, name) VALUES ('treatments', 'Treatments Page')");
        
        // Seed some default content for 'index'
        $insertContent = $pdo->prepare("INSERT INTO page_content (page_slug, section_key, label, content_type, content_value) VALUES (?, ?, ?, ?, ?)");
        
        $defaultIndex = [
            ['index', 'hero_title', 'Hero Title', 'text', 'Dr. Priya <em class="font-light italic text-inkmute">Jain</em>'],
            ['index', 'hero_subtitle', 'Hero Subtitle', 'textarea', '"We do not treat skin as a canvas for cosmetic trends. We treat it as a vital biological organ that flourishes under precision diagnosis and empathetic medical care."'],
            ['index', 'about_text', 'About Us Text', 'textarea', 'As the visionary founder of Medshine Clinic, Dr. Priya Jain (MBBS, FFAC Fellowships) has dedicated over 15 years to advancing clinical cosmetology and aesthetic services. As a renowned Skin Specialist and Aesthetic Physician, her evidence-based philosophy emphasizes cellular skin health, precision diagnostics, and tailored non-invasive rejuvenation.']
        ];

        foreach ($defaultIndex as $row) {
            $insertContent->execute($row);
        }
        echo "Created pages and seeded default content.<br>";
    }

    // Check if admin user exists
    $stmt = $pdo->query("SELECT * FROM users");
    if ($stmt->rowCount() == 0) {
        $defaultPassword = password_hash('admin123', PASSWORD_DEFAULT);
        $insert = $pdo->prepare("INSERT INTO users (email, password) VALUES (?, ?)");
        $insert->execute(['admin@medshineclinic.com', $defaultPassword]);
        echo "Created default admin user: admin@medshineclinic.com / admin123<br>";
    }

    echo "Database initialized successfully!";
} catch(PDOException $e) {
    echo "Error: " . $e->getMessage();
}
?>
