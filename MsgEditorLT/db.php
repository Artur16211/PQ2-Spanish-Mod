<?php

$servername = 'localhost';
$username = 'root';
$password = 'root';
$dbname = 'msgweb';

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    echo "Conexión fallida: " . $conn->connect_error;
    die("Conexión fallida: " . $conn->connect_error);
}
?>
