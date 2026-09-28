<?php
header('Content-Type: application/json');
require 'config.php';

$method = $_SERVER['REQUEST_METHOD'];
$slug = $_GET['slug'] ?? null;

if (!$slug) {
    http_response_code(400);
    echo json_encode(["error" => "Page slug is required"]);
    exit;
}

if ($method === 'GET') {
    // Both public and admin can GET page content (for the frontend to use via AJAX if needed, though we will use PHP directly)
    $stmt = $pdo->prepare("SELECT * FROM page_content WHERE page_slug = ?");
    $stmt->execute([$slug]);
    
    // For the admin panel, we return the full rows (label, type, value, key)
    if (isset($_GET['admin']) && isset($_SESSION['admin_id'])) {
        echo json_encode($stmt->fetchAll(PDO::FETCH_ASSOC));
    } else {
        // For public frontend (if they fetch via JS), just return key-value pairs
        $content = [];
        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
            $content[$row['section_key']] = $row['content_value'];
        }
        echo json_encode($content);
    }
} 
elseif ($method === 'PUT') {
    // Requires auth
    if (!isset($_SESSION['admin_id'])) {
        http_response_code(401);
        echo json_encode(["error" => "Unauthorized"]);
        exit;
    }

    $data = json_decode(file_get_contents("php://input"), true);
    
    if (!$data || !is_array($data)) {
        http_response_code(400);
        echo json_encode(["error" => "Invalid payload"]);
        exit;
    }

    $pdo->beginTransaction();
    try {
        $stmt = $pdo->prepare("UPDATE page_content SET content_value = ? WHERE page_slug = ? AND section_key = ?");
        foreach ($data as $key => $value) {
            $stmt->execute([$value, $slug, $key]);
        }
        $pdo->commit();
        echo json_encode(["message" => "Page saved successfully"]);
    } catch (Exception $e) {
        $pdo->rollBack();
        http_response_code(500);
        echo json_encode(["error" => $e->getMessage()]);
    }
} else {
    http_response_code(405);
    echo json_encode(["error" => "Method not allowed"]);
}
?>
