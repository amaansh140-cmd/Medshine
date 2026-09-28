<?php
header('Content-Type: application/json');
require 'config.php';

$method = $_SERVER['REQUEST_METHOD'];

if ($method === 'GET') {
    // Get all blogs
    $stmt = $pdo->query("SELECT * FROM blogs ORDER BY created_at DESC");
    echo json_encode($stmt->fetchAll(PDO::FETCH_ASSOC));
} 
elseif ($method === 'POST') {
    // Create new blog (requires auth)
    if (!isset($_SESSION['admin_id'])) {
        http_response_code(401);
        echo json_encode(["error" => "Unauthorized"]);
        exit;
    }

    $data = json_decode(file_get_contents("php://input"));
    $stmt = $pdo->prepare("INSERT INTO blogs (title, category, read_time, image, content) VALUES (?, ?, ?, ?, ?)");
    try {
        $stmt->execute([$data->title, $data->category, $data->read_time, $data->image, $data->content]);
        echo json_encode(["id" => $pdo->lastInsertId(), "message" => "Blog created successfully"]);
    } catch(PDOException $e) {
        http_response_code(500);
        echo json_encode(["error" => $e->getMessage()]);
    }
}
?>
