<?php

require_once 'db.php';

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['file'])) {
    $fileName = $_POST['file'];
    $fileName = str_replace('//', '/', $fileName);
    $fileName = str_replace('DATA', '', $fileName);

    try {
        // Check if a record exists with the provided file name
        $checkQuery = "SELECT COUNT(*) AS count FROM msgfile WHERE msg_filename = ?";
        $checkStmt = $conn->prepare($checkQuery);

        if ($checkStmt === false) {
            die("Error preparing query: " . $conn->error);
        }

        $checkStmt->bind_param("s", $fileName);
        $checkStmt->execute();
        $checkResult = $checkStmt->get_result()->fetch_assoc();

        if ($checkResult['count'] == 0) {
            // If no record exists, insert a new record
            $insertQuery = "INSERT INTO msgfile (msg_filename, updated_at, status) VALUES (?, CURRENT_TIMESTAMP, 3)";
            $insertStmt = $conn->prepare($insertQuery);

            if ($insertStmt === false) {
                die("Error preparing insert query: " . $conn->error);
            }

            $insertStmt->bind_param("s", $fileName);
            if ($insertStmt->execute() === false) {
                die("Error executing insert query: " . $insertStmt->error);
            }
        } else {
            // Update modification date in the database
            $updateQuery = "UPDATE msgfile SET updated_at = CURRENT_TIMESTAMP, status = 3 WHERE msg_filename = ?";
            $updateStmt = $conn->prepare($updateQuery);

            if ($updateStmt === false) {
                die("Error preparing update query: " . $conn->error);
            }

            $updateStmt->bind_param("s", $fileName);
            if ($updateStmt->execute() === false) {
                die("Error executing update query: " . $updateStmt->error);
            }

            echo "Modification date updated successfully in the database.";
        }
    } catch (Exception $e) {
        die("Error: " . $e->getMessage());
    } finally {
        // Close statements and connection
        if (isset($checkStmt)) $checkStmt->close();
        if (isset($insertStmt)) $insertStmt->close();
        if (isset($updateStmt)) $updateStmt->close();
        $conn->close();
    }
} else {
    echo "Invalid request.";
}
?>
