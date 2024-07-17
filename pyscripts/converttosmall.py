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

# Function to convert text based on conversion type
def convert_text(text, conversion_type):
    converted_text = ""
    if conversion_type == 'D':  # Convert from small font to default
        for char in text:
            if char in small_font:
                converted_text += small_font[char]
            else:
                converted_text += char
    elif conversion_type == 'S':  # Convert from default to small font
        reversed_small_font = {v: k for k, v in small_font.items()}
        for char in text:
            if char in reversed_small_font:
                converted_text += reversed_small_font[char]
            else:
                converted_text += char
    return converted_text

# Ask the user whether to convert from small font to default or vice versa
conversion_type = input("Convert from (D)efault to Slim or from (S)lim to Default? (D/S): ").strip().upper()

if conversion_type in ['D', 'S']:
    # Prompt for text input
    text = input("Enter text to convert: ")

    # Convert the text based on the chosen conversion type
    converted_text = convert_text(text, conversion_type)

    # Print the converted text
    print("Converted text:", converted_text)
else:
    print("Invalid input. Please enter 'D' or 'S'.")

# Require the input of the user to close the program
input("Press Enter to close the program")