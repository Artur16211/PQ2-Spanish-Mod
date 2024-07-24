import os

# Mapa de caracteres para reemplazar
char_map = {
    'á': 'ホ',
    'é': '〒',
    'í': 'ボ',
    'ó': 'ポ',
    'ú': 'マ',
    '¿': 'メ',
    '¡': 'ム',
    'ñ': 'ワ',
    'Á': 'ミ',
    'É': '※',
    'Í': 'レ',
    'Ó': 'ロ',
    'Ú': 'ヮ',
    'Ñ': 'ヰ'
}

def replace_characters_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    for key, value in char_map.items():
        content = content.replace(key, value)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.msg'):
                file_path = os.path.join(root, file)
                replace_characters_in_file(file_path)

# Ruta de la carpeta que quieres procesar
folder_path = 'C:/Users/Artur/Documents/PQ2-Spanish-Mod/formats/manual_fixed/event'  # Cambia esto por la ruta de tu carpeta
process_folder(folder_path)
