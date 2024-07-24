import os

# Definimos el mapeo inverso
replacements = {
    'ゼ': 'ァ',
    'ソ': 'ア',
    'ゾ': 'ィ',
    'タ': 'イ',
    'ダ': 'ゥ',
    'チ': 'ウ',
    'ヂ': 'ェ',
    'ッ': 'エ',
    'ツ': 'ォ',
    'ヅ': 'オ',
    'ド': 'ク',
    'ナ': 'グ',
    'ィ': 'ケ',
    'エ': 'ゲ',
    'ア': 'コ',
    'ァ': 'ゴ',
    'デ': 'サ',
    'ト': 'ザ',
    'ゥ': 'シ',
    'イ': 'ジ',
    'ェ': 'ス',
    'ウ': 'ズ',
    'オ': 'ダ',
    'ォ': 'チ',
    'ガ': 'ヅ',
    'カ': 'テ',
    'テ': 'デ',
    'ゲ': 'ド',
    'グ': 'ナ',
    'ギ': 'モ'
}

# Crear mapeo temporal
temp_replacements = {original: f"__TEMP_{i}__" for i, original in enumerate(replacements.keys())}
final_replacements = {f"__TEMP_{i}__": replacement for i, replacement in enumerate(replacements.values())}

# Función para reemplazar el texto en un archivo
def replace_text_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Reemplazo temporal
    for original, temp in temp_replacements.items():
        content = content.replace(original, temp)
    
    # Reemplazo final
    for temp, replacement in final_replacements.items():
        content = content.replace(temp, replacement)
    
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

# Ruta de la carpeta
folder_path = 'C:/Users/Artur/Documents/PQ2-Spanish-Mod/formats/manual_fixed/event'  # Cambia esto por la ruta de tu carpeta

# Iterar sobre todos los archivos .txt en la carpeta
for filename in os.listdir(folder_path):
    if filename.endswith('.msg'):
        file_path = os.path.join(folder_path, filename)
        replace_text_in_file(file_path)

print("Reemplazo completo.")
