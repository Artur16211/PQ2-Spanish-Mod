import os

# Define el diccionario de reemplazos
replacements = {
    "茨": "á", "姻": "é", "胤": "í", "吋": "ó", "雨": "ú",
    "夷": "¿", "斡": "¡", "隠": "ñ", "威": "Á", "畏": "É",
    "緯": "Í", "遺": "Ó", "郁": "Ú", "謂": "Ñ"
}

# Función para reemplazar caracteres en un archivo
def replace_characters_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    for original, replacement in replacements.items():
        content = content.replace(original, replacement)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Función para procesar todos los archivos .txt en una carpeta
def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.msg'):
                file_path = os.path.join(root, file)
                replace_characters_in_file(file_path)

# Define la carpeta a procesar
folder_path = 'C:/Users/Artur/Documents/PQ2-Spanish-Mod/pyscripts/fixnewfont'  # Cambia esto por la ruta de tu carpeta

# Procesa la carpeta
process_folder(folder_path)
