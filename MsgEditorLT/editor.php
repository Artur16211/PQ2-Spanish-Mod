<?php
// Obtener el nombre del archivo de la URL
$filePath = isset($_GET['file']) ? $_GET['file'] : '';

$parentDir = dirname($filePath);

$originalFilePath = 'EN/' . ltrim($filePath, '/');
$editableFilePath = 'DATA/' . ltrim($filePath, '/');

$show_font = array(
    "茨" => "á",
    "姻" => "é",
    "胤" => "í",
    "吋" => "ó",
    "雨" => "ú",
    "隠" => "ñ",
    "夷" => "¿",
    "斡" => "¡",
    "威" => "Á",
    "畏" => "É",
    "緯" => "Í",
    "遺" => "Ó",
    "郁" => "Ú",
    "謂" => "Ñ"
);

$show_font_inverse = array_flip($show_font);
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title><?php echo basename($editableFilePath); ?></title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<style>
    .form-control{
        background-color: #272727;
        color: #fff;
        }
    .invi{
        background-color: dark;
    }
</style>
<body data-bs-theme="dark">
    <div class="container">
        <h2 class="my-4"><?php echo basename($editableFilePath); ?></h2>
        <div class="mb-3">
            <a class="btn btn-primary mt-2" href="index.php?dir=<?php echo $parentDir; ?>"><-</a>
            <button type="button" class="btn btn-warning" onclick="saveChanges()">Guardar Pendiente</button>
            <button type="button" class="btn btn-info" onclick="markAsCompleted()">Guardar Completado</button>
            <button type="button" class="btn btn-success" onclick="markAsRevisedV2()">Guardar Revisado V2</button>
        </div>
        <div class="row">
            <div class="col">
                <h3>Spanish</h3>
                <form id="editForm" method="post">
                <?php
                // Spanish
                if (file_exists($editableFilePath)) {
                    $editableContent = file($editableFilePath);
                    foreach ($editableContent as $index => $line) {
                        $cleanedLine = str_replace('[n]', ' ', $line);
                        $cleanedLine = strtr($cleanedLine, $show_font);
                        echo '<textarea class="no-newline form-control mb-2" name="editable[]" rows="1" style="resize: none; height: 70px;">' . htmlspecialchars($cleanedLine) . '</textarea>';
                    }
                } else {
                    echo "El archivo editable no existe: $editableFilePath";
                }
                ?>
                </form>
            </div>
            <script>
                document.addEventListener('DOMContentLoaded', (event) => {
                const textareas = document.querySelectorAll('.no-newline');

                textareas.forEach(function(textarea) {
                    // Verifica si el contenido está vacío al cargar
                    if (textarea.value.trim() === '') {
                        textarea.readOnly = true;
                    }

                    // Si empieza por [msg o [sel establece readonly
                    if (textarea.value.trim().startsWith('[msg') || textarea.value.trim().startsWith('[sel')) {
                        textarea.readOnly = true;
                    }
                    // Elimina los saltos de línea al cargar
                    textarea.value = textarea.value.replace(/\n/g, '');
                });
                
                textareas.forEach(textarea => {
                    // Prevent new lines on Enter key press
                    textarea.addEventListener('keydown', function(e) {
                        if (e.key === 'Enter') {
                            e.preventDefault();
                        }
                    });

                    // Remove new lines in real-time
                    textarea.addEventListener('input', function() {
                        this.value = this.value.replace(/\n/g, '');
                    });
                });
            });
            </script>
            <div class="col">
                <h3>English</h3>
                <?php
                // English
                if (file_exists($originalFilePath)) {
                    $originalContent = file($originalFilePath);
                    foreach ($originalContent as $index => $line) {
                        $cleanedLine = str_replace('[n]', ' ', $line);
                        echo '<textarea class="form-control mb-2" name="original[]" rows="1" readonly style="resize: none; height: 70px;">' . htmlspecialchars($cleanedLine) . '</textarea>';
                    }
                } else {
                    echo "El archivo original no existe: $originalFilePath";
                }
                ?>
            </div>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

    <script>

        function saveChanges() {
            var file = '<?php echo $editableFilePath; ?>';
            file = file.replace("//", "/");
            var outputLines = [];

            $('textarea[name="editable[]"]').each(function(index) {
                var line = $(this).val().replace(/\r?\n/g, ' '); // Reemplazar saltos de línea por espacios
                line = revertCharacters(line);
                outputLines.push(line);
            });

            var confirmation = confirm("¿Desea guardar los cambios en " + file + "?");

            if (confirmation) {
                $.ajax({
                    type: "POST",
                    url: "save_changes.php",
                    data: {
                        file: file,
                        lines: outputLines
                    },
                    success: function(response) {
                        alert(response);
                        updateDatabase(file);
                    },
                    error: function(xhr, status, error) {
                        console.error("Error al guardar los cambios:", error);
                    }
                });
            }
        }


        function markAsCompleted() {
            var file = '<?php echo $editableFilePath; ?>';
            file = file.replace("//", "/");
            var outputLines = [];

            $('input[name="editable[]"]').each(function(index) {
                var line = $(this).val();
                outputLines.push(line);
            });

            var confirmation = confirm("¿Guardar y marcar como completado: " + file + "?");

            if (confirmation) {
                $.ajax({
                    type: "POST",
                    url: "save_changes.php",
                    data: {
                        file: file,
                        lines: outputLines
                    },
                    success: function(response) {
                        alert(response);
                        markAsCompletedInDB(file);
                    },
                    error: function(xhr, status, error) {
                        console.error("Error al guardar los cambios:", error);
                    }
                });
            }
        }

        function markAsRevisedV2() {
            var file = '<?php echo $editableFilePath; ?>';
            file = file.replace("//", "/");
            var outputLines = [];

            $('input[name="editable[]"]').each(function(index) {
                var line = $(this).val();
                outputLines.push(line);
            });

            var confirmation = confirm("¿Guardar y marcar como revisado: " + file + "?");
            if (confirmation) {
                $.ajax({
                    type: "POST",
                    url: "save_changes.php",
                    data: {
                        file: file,
                        lines: outputLines
                    },
                    success: function(response) {
                        alert(response);
                        markAsRevisedInDB(file);
                    },
                    error: function(xhr, status, error) {
                        console.error("Error al guardar los cambios:", error);
                    }
                });
            }
        }

        function updateDatabase(file) {
            $.ajax({
                type: "POST",
                url: "update_db.php",
                data: {
                    file: file
                },
                success: function(response) {
                    console.log("Fecha de modificación actualizada en la base de datos.");
                },
                error: function(xhr, status, error) {
                    console.error("Error al actualizar la fecha de modificación en la base de datos:", error);
                }
            });
        }

        function markAsCompletedInDB(file) {
            $.ajax({
                type: "POST",
                url: "update_db_complete.php",
                data: {
                    file: file
                },
                success: function(response) {
                    console.log("Archivo marcado como completado en la base de datos.");
                },
                error: function(xhr, status, error) {
                    console.error("Error al marcar como completado en la base de datos:", error);
                }
            });
        }

        function markAsRevisedInDB(file) {
            $.ajax({
                type: "POST",
                url: "update_db_revised.php",
                data: {
                    file: file
                },
                success: function(response) {
                    console.log("Archivo marcado como revisado en la base de datos.");
                },
                error: function(xhr, status, error) {
                    console.error("Error al marcar como revisado en la base de datos:", error);
                }
            });
        }

        function revertCharacters(line) {
            var showFontInverse = <?php echo json_encode($show_font_inverse); ?>;
            for (var char in showFontInverse) {
                if (showFontInverse.hasOwnProperty(char)) {
                    var originalChar = showFontInverse[char];
                    var regex = new RegExp(char, 'g');
                    line = line.replace(regex, originalChar);
                }
            }
            return line;
        }
    </script>
</body>
</html>
