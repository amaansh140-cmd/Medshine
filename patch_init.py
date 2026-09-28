with open('public/api/init.php', 'r') as f:
    content = f.read()
    
with open('treatment_seeds.txt', 'r') as f:
    seeds = f.read()
    
new_table = """
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
    
    // Seed treatments
    $pdo->exec("INSERT IGNORE INTO treatments (category, slug, title, description, image) VALUES """ + seeds + """");
"""

content = content.replace('echo "Database initialized successfully!";', new_table + '\n    echo "Database initialized successfully!";')

with open('public/api/init.php', 'w') as f:
    f.write(content)
