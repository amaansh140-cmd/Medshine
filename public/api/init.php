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
