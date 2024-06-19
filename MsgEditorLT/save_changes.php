<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST['file'], $_POST['lines']) && is_array($_POST['lines'])) {
        $file = $_POST['file'];

        $filePath = $file;

        if (file_exists($filePath) && is_writable($filePath)) {
            $handle = fopen($filePath, "w");

            if ($handle !== false) {
                foreach ($_POST['lines'] as $line) {
                    // Eliminar cualquier salto de línea al final de la línea
                    $line = rtrim($line, "\r\n");
                    fwrite($handle, $line . PHP_EOL);
                }

                fclose($handle);

                echo "Los cambios se han guardado correctamente en $filePath.";
            } else {
                echo "Error al abrir el archivo $filePath para escribir.";
            }
        } else {
            echo "El archivo $filePath no existe o no se puede escribir en él.";
        }
    } else {
        echo "Datos del formulario inválidos.";
    }
} else {
    echo "Acceso no permitido.";
}
?>
