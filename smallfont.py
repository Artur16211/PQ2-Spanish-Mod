import os


def replace_chars_in_folder(folder_path, replacements):
    try:
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.msg'):
                file_path = os.path.join(folder_path, file_name)
                replace_chars_in_file(file_path, replacements)

        print("Replacements completed for all .msg files in the folder!")

    except FileNotFoundError:
        print("Folder not found.")
    except Exception as e:
        print("An error occurred:", str(e))


def replace_chars_in_file(file_path, replacements):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                new_line = ''
                inside_brackets = False
                for char in line:
                    if char == '[':
                        inside_brackets = True
                    elif char == ']':
                        inside_brackets = False

                    if not inside_brackets:
                        for old_char, new_char in replacements.items():
                            char = char.replace(old_char, new_char)
                    new_line += char

                file.write(new_line)

        print("Replacements completed for", file_path)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))


# Diccionario de reemplazos
replacements = {
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
    #
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
    # fix old font
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

# Ruta de la carpeta que contiene los archivos de texto
folder_path = r'C:\Users\Arthu\OneDrive\Escritorio\Nueva carpeta (2)'

# Llamar a la función para reemplazar caracteres en todos los archivos de texto en la carpeta
replace_chars_in_folder(folder_path, replacements)
