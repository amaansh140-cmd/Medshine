<?php
header('Cache-Control: no-store, no-cache, must-revalidate, max-age=0');
header('Cache-Control: post-check=0, pre-check=0', false);
header('Pragma: no-cache');
header('Content-Type: application/json');
require 'config.php';

$method = $_SERVER['REQUEST_METHOD'];

// Public GET for fetching treatments (optional, we use direct PHP mainly)
if ($method === 'GET') {
    if (isset($_GET['id'])) {
        $stmt = $pdo->prepare("SELECT * FROM treatments WHERE id = ?");
        $stmt->execute([$_GET['id']]);
        echo json_encode($stmt->fetch(PDO::FETCH_ASSOC));
    } else if (isset($_GET['cat'])) {
        $stmt = $pdo->prepare("SELECT * FROM treatments WHERE category = ? ORDER BY title ASC");
        $stmt->execute([$_GET['cat']]);
        echo json_encode($stmt->fetchAll(PDO::FETCH_ASSOC));
    } else {
        $stmt = $pdo->query("SELECT * FROM treatments ORDER BY category ASC, title ASC");
        echo json_encode($stmt->fetchAll(PDO::FETCH_ASSOC));
    }
    exit;
}

// Authentication required for POST/PUT/DELETE
if (!isset($_SESSION['admin_id'])) {
    http_response_code(401);
    echo json_encode(["error" => "Unauthorized"]);
    exit;
}

if ($method === 'POST') {
    $data = json_decode(file_get_contents("php://input"), true);
    
    // Auto-generate slug from title if missing
    $slug = $data['slug'] ?? strtolower(trim(preg_replace('/[^A-Za-z0-9-]+/', '-', $data['title']), '-'));
    
    $stmt = $pdo->prepare("INSERT INTO treatments (category, slug, title, description, image) VALUES (?, ?, ?, ?, ?)");
    try {
        $stmt->execute([$data['category'], $slug, $data['title'], $data['description'], $data['image'] ?? '']);
        echo json_encode(["id" => $pdo->lastInsertId(), "message" => "Treatment added"]);
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(["error" => $e->getMessage()]);
    }
} 
elseif ($method === 'PUT') {
    $data = json_decode(file_get_contents("php://input"), true);
    $id = $_GET['id'] ?? null;
    
    if (!$id) {
        http_response_code(400);
        echo json_encode(["error" => "ID required"]);
        exit;
    }
    
    $slug = $data['slug'] ?? strtolower(trim(preg_replace('/[^A-Za-z0-9-]+/', '-', $data['title']), '-'));

    $stmt = $pdo->prepare("UPDATE treatments SET category=?, slug=?, title=?, description=?, image=? WHERE id=?");
    try {
        $stmt->execute([$data['category'], $slug, $data['title'], $data['description'], $data['image'] ?? '', $id]);
        echo json_encode(["message" => "Treatment updated"]);
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(["error" => $e->getMessage()]);
    }
} 
elseif ($method === 'DELETE') {
    $id = $_GET['id'] ?? null;
    if (!$id) {
        http_response_code(400);
        echo json_encode(["error" => "ID required"]);
        exit;
    }
    
    $stmt = $pdo->prepare("DELETE FROM treatments WHERE id=?");
    $stmt->execute([$id]);
    echo json_encode(["message" => "Treatment deleted"]);
} else {
    http_response_code(405);
    echo json_encode(["error" => "Method not allowed"]);
}
?>
