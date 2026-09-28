<?php
session_start();

$db_host = 'localhost';
$db_name = 'u600893894_cms';
$db_user = 'u600893894_cmsuser';
$db_pass = 'Medshine@1232';

try {
    $pdo = new PDO("mysql:host=$db_host;dbname=$db_name;charset=utf8", $db_user, $db_pass);
    // Set PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    die(json_encode(["error" => "Connection failed: " . $e->getMessage()]));
}
?>
