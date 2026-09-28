<?php
header('Content-Type: application/json');
require 'config.php';

if (isset($_SESSION['admin_id'])) {
    echo json_encode(["authenticated" => true]);
} else {
    http_response_code(401);
    echo json_encode(["error" => "Not authenticated"]);
}
?>
