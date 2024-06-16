import re

# small_font = {
#     'A': 'だ',
#     'B': 'ち',
#     'C': 'ぢ',
#     'D': 'っ',
#     'E': 'つ',
#     'F': 'づ',
#     'G': 'て',
#     'H': 'で',
#     'I': 'と',
#     'J': 'ど',
#     'K': 'な',
#     'L': 'に',
#     'M': 'ぬ',
#     'N': 'ね',
#     'O': 'の',
#     'P': 'は',
#     'Q': 'ば',
#     'R': 'ぱ',
#     'S': 'ひ',
#     'T': 'び',
#     'U': 'ぴ',
#     'V': 'ふ',
#     'W': 'ぶ',
#     'X': 'ぷ',
#     'Y': 'へ',
#     'Z': 'べ',
#     'a': 'ぺ',
#     'b': 'ほ',
#     'c': 'ぼ',
#     'd': 'ぽ',
#     'e': 'ま',
#     'f': 'み',
#     'g': 'む',
#     'h': 'め',
#     'i': 'も',
#     'j': 'ゃ',
#     'k': 'や',
#     'l': 'ゅ',
#     'm': 'ゆ',
#     'n': 'ょ',
#     'o': 'よ',
#     'p': 'ら',
#     'q': 'り',
#     'r': 'る',
#     's': 'れ',
#     't': 'ろ',
#     'u': 'ゎ',
#     'v': 'わ',
#     'w': 'ゐ',
#     'x': 'ゑ',
#     'y': 'を',
#     'z': 'ん',
#     'á': 'ァ',
#     'Á': 'ア',
#     '¡': 'ィ',
#     'é': 'イ',
#     'É': 'ゥ',
#     'í': 'ウ',
#     'Í': 'ェ',
#     '¿': 'エ',
#     'ñ': 'ォ',
#     'Ñ': 'オ',
#     'ó': 'カ',
#     'Ó': 'ガ',
#     '/': 'ギ',
#     'ú': 'グ',
#     'Ú': 'ゲ',
#     '0': 'ゼ',
#     '1': 'ソ',
#     '2': 'ゾ',
#     '3': 'タ',
#     '4': 'ダ',
#     '5': 'チ',
#     '6': 'ヂ',
#     '7': 'ッ',
#     '8': 'ツ',
#     '9': 'ヅ',
#     '.': 'テ',
#     ',': 'デ',
#     ':': 'ト',
#     '(': 'ド',
#     ')': 'ナ',
#     #
#     '位': 'グ',
#     '案': 'カ',
#     '按': 'ォ',
#     #
#     '茨': 'ァ',
#     '姻': 'イ',
#     '胤': 'ウ',
#     '吋': 'カ',
#     '雨': 'グ',
#     '隠': 'ォ',
#     '夷': 'エ',
#     '斡': 'ィ',
#     '威': 'ア',
#     '畏': 'ゥ',
#     '緯': 'ェ',
#     '遺': 'ガ',
#     '郁': 'ゲ',
#     '謂': 'オ'
# }


# def clean_dialogues(line):
#     pattern = r'\[[^\[\]]+\](?:\[[^\[\]]+\])+'
#     clean_line = re.sub(pattern, '', line)
#     clean_line = re.sub(r'\[n\]', ' ', clean_line)
#     # delete [e]
#     clean_line = re.sub(r'\[e\]', '', clean_line)
#     clean_line = re.sub(r'\s+', ' ', clean_line).strip()
#     return clean_line


def set_n(text, max_length):
    ignore_chars = r'[~^@{}ŽŠ]'
    words = text.split()
    current_line = ''
    result = ''
    current_characters = 0

    for word in words:
        cleaned_word = re.sub(ignore_chars, '', word)
        if current_characters + len(cleaned_word) + (1 if current_line else 0) > max_length:
            result += current_line + '[n]'
            current_line = word
            current_characters = len(cleaned_word)
        else:
            if current_line:
                current_line += ' ' + word
                current_characters += len(cleaned_word) + 1
            else:
                current_line = word
                current_characters = len(cleaned_word)

    if current_line:
        result += current_line

    return result


# def process_text(text, max_length):
#     cleaned_text = clean_dialogues(text)
#     transformed_text = set_n(cleaned_text, max_length)

#     if transformed_text.count('[n]') > 2:
#         transformed_text = ''.join(small_font.get(c, c) for c in cleaned_text)
#         transformed_text = set_n(transformed_text, 46)

#     return transformed_text


# text = '[f 0 5 65278][f 2 1][f 3 1 1 0 0 0]Quiero decir, sospechaba que ten胤a[n]varias fans secretas en la escuela, pero[n]pensar que me encontrar胤a con una[n]aqu胤...[n][f 1 3 65535][f 1 1][e]'
# max_length = 40

# final_text = process_text(text, max_length)
# print(final_text)
