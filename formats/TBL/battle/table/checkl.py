import re
import os
special_chars = "↓※〒ホボポマミレロヮワヰムメ"

combined_pattern = f"ｶ[{re.escape(special_chars)}]"

small_font = {
    'A': 'だ', 'B': 'ち', 'C': 'ぢ', 'D': 'っ', 'E': 'つ', 'F': 'づ', 'G': 'て', 'H': 'で', 'I': 'と', 'J': 'ど',
    'K': 'な', 'L': 'に', 'M': 'ぬ', 'N': 'ね', 'O': 'の', 'P': 'は', 'Q': 'ば', 'R': 'ぱ', 'S': 'ひ', 'T': 'び',
    'U': 'ぴ', 'V': 'ふ', 'W': 'ぶ', 'X': 'ぷ', 'Y': 'へ', 'Z': 'べ', 'a': 'ぺ', 'b': 'ほ', 'c': 'ぼ', 'd': 'ぽ',
    'e': 'ま', 'f': 'み', 'g': 'む', 'h': 'め', 'i': 'も', 'j': 'ゃ', 'k': 'や', 'l': 'ゅ', 'm': 'ゆ', 'n': 'ょ',
    'o': 'よ', 'p': 'ら', 'q': 'り', 'r': 'る', 's': 'れ', 't': 'ろ', 'u': 'ゎ', 'v': 'わ', 'w': 'ゐ', 'x': 'ゑ',
    'y': 'を', 'z': 'ん', '0': 'ァ', '1': 'ア', '2': 'ィ', '3': 'イ', '4': 'ゥ', '5': 'ウ', '6': 'ェ', '7': 'エ',
    '8': 'ォ', '9': 'オ', '(': 'ク', ')': 'グ', '/': 'モ', '?': 'ャ', '!': 'ヤ', '¡': 'ケ', '¿': 'ゲ', 'Á': 'コ',
    'á': 'ゴ', ',': 'サ', ':': 'ザ', 'É': 'シ', 'é': 'ジ', 'Í': 'ス', 'í': 'ズ', 'Ñ': 'ダ', 'ñ': 'チ', 'Ó': 'ヅ',
    'ó': 'テ', '.': 'デ', 'Ú': 'ド', 'ú': 'ナ', 'ホ': 'ゴ', '〒': 'ジ', 'ボ': 'ズ', 'ポ': 'テ', 'マ': 'ナ', 'ワ': 'チ',
    'ム': 'ケ', 'メ': 'ゲ', 'ミ': 'コ', '※': 'シ', 'レ': 'ス', 'ロ': 'ヅ', 'ヮ': 'ド', 'ヰ': 'ダ'
}
replace_pattern = re.compile('|'.join(map(re.escape, small_font.keys())))

def replace_characters(line):
    return replace_pattern.sub(lambda match: small_font[match.group(0)], line)

def count_characters(line):
    line_normalized = re.sub(combined_pattern, "X", line)
    line_normalized = re.sub(f"[{re.escape(special_chars)}]", " ", line_normalized)
    return len(line_normalized)

def process_file(input_file_path, temp_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as infile, open(temp_file_path, 'w', encoding='utf-8') as temp_file:
        for line in infile:
            if count_characters(line) > 17:
                line = replace_characters(line)
            temp_file.write(line)

    os.replace(temp_file_path, input_file_path)

process_file('skillnametable.ebl', 'skillnametable_rep.ebl')
