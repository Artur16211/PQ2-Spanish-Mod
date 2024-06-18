<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MSG Editor - Q2</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body data-bs-theme="dark">
<div class="container mt-5">
    <?php

require_once 'db.php';

function showNavigation($currentPath)
{
    $parts = explode('/', $currentPath);
    $path = '';

    echo "<label>";

    echo "<a href='index.php'>Inicio</a> / ";

    if (empty($parts[0])) {
        array_shift($parts);
    }

    foreach ($parts as $part) {
        if (!empty($part)) {
            $path .= $part . '/';
            echo "<a href='index.php?dir=$path'>$part</a>";
            echo " / ";
        }
    }

    echo "</label>";
}

function formatSizeUnits($bytes)
{
    if ($bytes >= 1073741824) {
        $bytes = number_format($bytes / 1073741824, 2) . ' GB';
    } elseif ($bytes >= 1048576) {
        $bytes = number_format($bytes / 1048576, 2) . ' MB';
    } elseif ($bytes >= 1024) {
        $bytes = number_format($bytes / 1024, 2) . ' KB';
    } elseif ($bytes > 1) {
        $bytes = $bytes . ' bytes';
    } elseif ($bytes == 1) {
        $bytes = $bytes . ' byte';
    } else {
        $bytes = '0 bytes';
    }

    return $bytes;
}

$currentPath = isset($_GET['dir']) ? $_GET['dir'] : '';
$directory = 'data/' . $currentPath;

date_default_timezone_set('America/Mexico_City');

showNavigation($currentPath);

if (is_dir($directory)) {
    echo "<h2>$directory</h2>";
    echo "<ul class='list-group'>";

    $items = array_diff(scandir($directory), array('.', '..'));
    foreach ($items as $item) {
        $path = $directory . '/' . $item;
        if (is_dir($path)) {
            echo "<li class='list-group-item'><a href='index.php?dir=$currentPath/$item'>$item/</a></li>";
        } elseif (is_file($path) && pathinfo($path, PATHINFO_EXTENSION) == 'msg') {
            $size = filesize($path);
            $sizeFormatted = formatSizeUnits($size);

            $file_name = $currentPath . '/' . $item;
            $file_name = str_replace('//', '/', $file_name);

            if ($file_name[0] != '/') {
                $file_name = '/' . $file_name;
            }

            $sql = "SELECT updated_at, status FROM msgfile WHERE msg_filename = ?";
            $stmt = $conn->prepare($sql);
            $stmt->bind_param("s", $file_name);
            $stmt->execute();
            $stmt->bind_result($updated_at, $status);

            if ($stmt->fetch()) {
                $last_modified = date("d/m/Y H:i:s", strtotime($updated_at));
                $estado = '';
                if ($status == 1) {
                    $estado = "list-group-item-dark"; // Sin revisar
                } elseif ($status == 2) {
                    $estado = "list-group-item-warning"; // Pendiente
                } elseif ($status == 3) {
                    $estado = "list-group-item-info"; // Completado
                } elseif ($status == 4) {
                    $estado = "list-group-item-success"; // Completado revisado
                }
                echo "<li class='list-group-item $estado'><a href='editor.php?file=$currentPath/$item'>$item</a> ($sizeFormatted) <span class='text-muted'>Modificado: $last_modified</span></li>";
            } else {
                echo "<li class='list-group-item list-group-item-dark'><a href='editor.php?file=$currentPath/$item'>$item</a> ($sizeFormatted) <span class='text-muted'></span></li>";
            }
            $stmt->close();
        }
    }
    echo "</ul>";
} else {
    echo "<p>El directorio '$directory' no existe.</p>";
}
?>



    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
        </div>
</body>

</html>
