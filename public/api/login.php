<?php
header('Content-Type: application/json');
require 'config.php';

$data = json_decode(file_get_contents("php://input"));

if (!isset($data->email) || !isset($data->password)) {
    http_response_code(400);
    echo json_encode(["error" => "Email and password required"]);
    exit;
}

$stmt = $pdo->prepare("SELECT * FROM users WHERE email = ?");
$stmt->execute([$data->email]);
$user = $stmt->fetch();

if ($user && password_verify($data->password, $user['password'])) {
    $_SESSION['admin_id'] = $user['id'];
    echo json_encode(["message" => "Login successful"]);
} else {
    http_response_code(401);
    echo json_encode(["error" => "Invalid credentials"]);
}
?>
