import os

# Diccionario de fuente small a fuente normal
small_font = {
    'A': 'だ',
    'B': 'ち',
    'C': 'ぢ',
    'D': 'っ',
    'E': 'つ',
    'F': 'づ',
    'G': 'て',
    'H': 'で',
    'I': 'と',
    'J': 'ど',
    'K': 'な',
    'L': 'に',
    'M': 'ぬ',
    'N': 'ね',
    'O': 'の',
    'P': 'は',
    'Q': 'ば',
    'R': 'ぱ',
    'S': 'ひ',
    'T': 'び',
    'U': 'ぴ',
    'V': 'ふ',
    'W': 'ぶ',
    'X': 'ぷ',
    'Y': 'へ',
    'Z': 'べ',
    'a': 'ぺ',
    'b': 'ほ',
    'c': 'ぼ',
    'd': 'ぽ',
    'e': 'ま',
    'f': 'み',
    'g': 'む',
    'h': 'め',
    'i': 'も',
    'j': 'ゃ',
    'k': 'や',
    'l': 'ゅ',
    'm': 'ゆ',
    'n': 'ょ',
    'o': 'よ',
    'p': 'ら',
    'q': 'り',
    'r': 'る',
    's': 'れ',
    't': 'ろ',
    'u': 'ゎ',
    'v': 'わ',
    'w': 'ゐ',
    'x': 'ゑ',
    'y': 'を',
    'z': 'ん',
    'á': 'ァ',
    'Á': 'ア',
    '¡': 'ィ',
    'é': 'イ',
    'É': 'ゥ',
    'í': 'ウ',
    'Í': 'ェ',
    '¿': 'エ',
    'ñ': 'ォ',
    'Ñ': 'オ',
    'ó': 'カ',
    'Ó': 'ガ',
    '/': 'ギ',
    'ú': 'グ',
    'Ú': 'ゲ',
    '0': 'ゼ',
    '1': 'ソ',
    '2': 'ゾ',
    '3': 'タ',
    '4': 'ダ',
    '5': 'チ',
    '6': 'ヂ',
    '7': 'ッ',
    '8': 'ツ',
    '9': 'ヅ',
    '.': 'テ',
    ',': 'デ',
    ':': 'ト',
    '(': 'ド',
    ')': 'ナ',
    #
    '位': 'グ',
    '案': 'カ',
    '按': 'ォ',
    #
    '茨': 'ァ',
    '姻': 'イ',
    '胤': 'ウ',
    '吋': 'カ',
    '雨': 'グ',
    '隠': 'ォ',
    '夷': 'エ',
    '斡': 'ィ',
    '威': 'ア',
    '畏': 'ゥ',
    '緯': 'ェ',
    '遺': 'ガ',
    '郁': 'ゲ',
    '謂': 'オ'
}

# Función para revertir la fuente small a la fuente normal
def revert_font(text, font_dict):
    reverted_text = ""
    reversed_font_dict = {v: k for k, v in font_dict.items()}
    for char in text:
        if char in reversed_font_dict:
            reverted_text += reversed_font_dict[char]
        else:
            reverted_text += char
    return reverted_text

# Función para procesar archivos en una carpeta y sus subcarpetas
def process_files(root_folder, font_dict):
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.msg'):
                file_path = os.path.join(foldername, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                reverted_content = revert_font(content, font_dict)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(reverted_content)
                print(f"Processed file: {file_path}")

# Ruta de la carpeta principal (cambiar según sea necesario)
root_folder = 'C:/Users/Artur/Documents/PQ2-Spanish-Mod/MsgEditorLT/Data'

# Ejecutar el procesamiento de archivos
process_files(root_folder, small_font)
