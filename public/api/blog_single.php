<?php
header('Content-Type: application/json');
require 'config.php';

// Requires auth
if (!isset($_SESSION['admin_id'])) {
    http_response_code(401);
    echo json_encode(["error" => "Unauthorized"]);
    exit;
}

$method = $_SERVER['REQUEST_METHOD'];
$id = $_GET['id'] ?? null;

if (!$id) {
    http_response_code(400);
    echo json_encode(["error" => "ID is required"]);
    exit;
}

if ($method === 'PUT') {
    $data = json_decode(file_get_contents("php://input"));
    $stmt = $pdo->prepare("UPDATE blogs SET title = ?, category = ?, read_time = ?, image = ?, content = ? WHERE id = ?");
    try {
        $stmt->execute([$data->title, $data->category, $data->read_time, $data->image, $data->content, $id]);
        echo json_encode(["message" => "Blog updated successfully"]);
    } catch(PDOException $e) {
        http_response_code(500);
        echo json_encode(["error" => $e->getMessage()]);
    }
} 
elseif ($method === 'DELETE') {
    $stmt = $pdo->prepare("DELETE FROM blogs WHERE id = ?");
    try {
        $stmt->execute([$id]);
        echo json_encode(["message" => "Blog deleted successfully"]);
    } catch(PDOException $e) {
        http_response_code(500);
        echo json_encode(["error" => $e->getMessage()]);
    }
}
?>
