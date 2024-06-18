<?php
require_once 'db.php';

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['file'])) {
    $fileName = $_POST['file'];
    $fileName = str_replace('//', '/', $fileName);
    $fileName = str_replace('DATA', '', $fileName);

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Conexión fallida: " . $conn->connect_error);
    } else {
        echo "Conexión exitosa";
    }

    try {
        $checkQuery = "SELECT COUNT(*) AS count FROM msgfile WHERE msg_filename = ?";
        $checkStmt = $conn->prepare($checkQuery);
        
        if ($checkStmt === false) {
            die("Error en la preparación de la consulta: " . $conn->error);
        }
        
        $checkStmt->bind_param("s", $fileName);
        $checkStmt->execute();
        $checkResult = $checkStmt->get_result()->fetch_assoc();
        
        if ($checkResult['count'] == 0) {
            $insertQuery = "INSERT INTO msgfile (msg_filename, updated_at, status) VALUES (?, CURRENT_TIMESTAMP, 2)";
            $insertStmt = $conn->prepare($insertQuery);
            
            if ($insertStmt === false) {
                die("Error en la preparación de la consulta de inserción: " . $conn->error);
            }
            
            $insertStmt->bind_param("s", $fileName);
            if ($insertStmt->execute() === false) {
                die("Error al ejecutar la consulta de inserción: " . $insertStmt->error);
            }
        } else {
            $updateQuery = "UPDATE msgfile SET updated_at = CURRENT_TIMESTAMP, status = 2 WHERE msg_filename = ?";
            $updateStmt = $conn->prepare($updateQuery);
            
            if ($updateStmt === false) {
                die("Error en la preparación de la consulta de actualización: " . $conn->error);
            }
            
            $updateStmt->bind_param("s", $fileName);
            if ($updateStmt->execute() === false) {
                die("Error al ejecutar la consulta de actualización: " . $updateStmt->error);
            }
            
            echo "La fecha de modificación se ha actualizado correctamente en la base de datos.";
        }
    } catch (Exception $e) {
        die("Error: " . $e->getMessage());
    } finally {
        if (isset($checkStmt)) $checkStmt->close();
        if (isset($insertStmt)) $insertStmt->close();
        if (isset($updateStmt)) $updateStmt->close();
        $conn->close();
    }
} else {
    echo "Petición no válida.";
}
?>
