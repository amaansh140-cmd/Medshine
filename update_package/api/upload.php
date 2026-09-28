<?php
header('Cache-Control: no-store, no-cache, must-revalidate, max-age=0');
header('Cache-Control: post-check=0, pre-check=0', false);
header('Pragma: no-cache');
header('Content-Type: application/json');
require 'config.php';

// Requires auth
if (!isset($_SESSION['admin_id'])) {
    http_response_code(401);
    echo json_encode(["error" => "Unauthorized"]);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(["error" => "Method not allowed"]);
    exit;
}

if (!isset($_FILES['file'])) {
    http_response_code(400);
    echo json_encode(["error" => "No file uploaded"]);
    exit;
}

$file = $_FILES['file'];
$uploadDir = '../uploads/'; // Goes to public/uploads/ -> which becomes dist/uploads/
if (!is_dir($uploadDir)) {
    mkdir($uploadDir, 0755, true);
}

$fileName = time() . '_' . basename($file['name']);
$targetPath = $uploadDir . $fileName;

// Basic validation
$allowedTypes = ['image/jpeg', 'image/png', 'image/webp', 'image/gif', 'video/mp4'];
if (!in_array($file['type'], $allowedTypes)) {
    http_response_code(400);
    echo json_encode(["error" => "Invalid file type. Only JPG, PNG, WEBP, GIF, and MP4 allowed."]);
    exit;
}

if (move_uploaded_file($file['tmp_name'], $targetPath)) {
    // Return the URL relative to the domain root
    $publicUrl = '/uploads/' . $fileName;
    echo json_encode(["url" => $publicUrl, "message" => "Upload successful"]);
} else {
    http_response_code(500);
    echo json_encode(["error" => "Failed to save file"]);
}
?>
