import os
import re
from addn import set_n
import logging

logging.basicConfig(level=logging.INFO)

fixparamsindialog = {
    '[f 6 1 12 0 0 0]': 'P4MCN1',
    '[f 6 1 13 0 0 0]': 'P4MCN2',
    '[f 6 1 15 0 0 0]': 'P3MCN1',
    '[f 6 1 16 0 0 0]': 'P3MCN2',
    '[f 6 1 16 0 0]': 'P3MCN2',
    '[f 6 1 26 0 0 0]': 'P3FEM1',
    '[f 6 1 27 0 0 0]': 'P3FEM2',
    '[f 6 1 29 0 0 0]': 'P5MCN1',
    '[f 6 1 30 0 0 0]': 'P5MCN2',
    '[f 4 4 3 0 1333]': 'OBJETON5',
    '[f 4 4 3 0 1350]': 'OBJETONUMEROOBJ1',
    '[f 4 4 3 0 1593]': 'OBJETONUMEROOBJ2',
    '[f 4 4 3 0 1595]': 'OBJETONUMEROOBJ3',
    '[f 4 4 3 0 1596]': 'OBJETONUMEROOBJ4',
    '[f 2 5 3 65535 0]': 'OBJETONUMEROOBJ5',
    '[f 0 7 0 65535]': 'OBJETONUMEROOBJ6',
    '[f 0 7 150 65535]': 'OBJETONUMEROOBJ7',
    '[f 2 5 3 65535 1]': 'OBJETONUMEROOBJ8',
    '[f 2 5 3 65535 2]': 'OBJETONUMEROOBJ9',
    '[f 2 5 3 65535 3]': 'OBJETONUMEROOBJ0',
    '[f 3 1 1 0 0 59203]': 'OBJETONUMEROOBJX',
    '[f 4 4 3 0 1636]': 'WEAPONNUMERO1',
    '[f 4 4 3 0 1637]': 'WEAPONNUMERO2',
    '[f 4 4 3 0 1637]': 'WEAPONNUMERO3',
    '[f 2 4 0]': 'PERSONANAMENUM1',
    '[f 2 4 1]': 'PERSONANAMENUM2',
    '[f 2 4 2]': 'DMG1',
    '[f 2 4 3]': 'PERSONASKILLNUM1',
    '[f 0 1 1]': '~',
    '[f 0 1 2]': '^',
    '[f 0 1 3]': '@',
    '[f 0 1 4]': '{',
    '[f 0 1 0]': '}',
    '[f 0 1 5]': 'Ž',
    '[f 0 1 8]': 'Š',
    # Slim font
    '[f 6 1 12 0 0 0]': "はダぬぢねソ",
    '[f 6 1 13 0 0 0]': "はダぬぢねゾ",
    '[f 6 1 15 0 0 0]': "はタぬぢねソ",
    '[f 6 1 16 0 0 0]': "はタぬぢねゾ",
    '[f 6 1 16 0 0]': "はタぬぢねゾ",
    '[f 6 1 26 0 0 0]': "はタづつぬソ",
    '[f 6 1 27 0 0 0]': "はタづつぬゾ",
    '[f 6 1 29 0 0 0]': "はチぬぢねソ",
    '[f 6 1 30 0 0 0]': "はチぬぢねゾ",
    '[f 4 4 3 0 1333]': "のちどつびのねチ",
    '[f 4 4 3 0 1350]': "のちどつびのねぴぬつぱののちどソ",
    '[f 4 4 3 0 1593]': "のちどつびのねぴぬつぱののちどゾ",
    '[f 4 4 3 0 1595]': "のちどつびのねぴぬつぱののちどタ",
    '[f 4 4 3 0 1596]': "のちどつびのねぴぬつぱののちどダ",
    '[f 2 5 3 65535 0]': "のちどつびのねぴぬつぱののちどチ",
    '[f 0 7 0 65535]': "のちどつびのねぴぬつぱののちどヂ",
    '[f 0 7 150 65535]': "のちどつびのねぴぬつぱののちどッ",
    '[f 2 5 3 65535 1]': "のちどつびのねぴぬつぱののちどツ",
    '[f 2 5 3 65535 2]': "のちどつびのねぴぬつぱののちどヅ",
    '[f 2 5 3 65535 3]': "のちどつびのねぴぬつぱののちどゼ",
    '[f 3 1 1 0 0 59203]': "のちどつびのねぴぬつぱののちどぷ",
    '[f 4 4 3 0 1636]': "ぶつだはのねねぴぬつぱのソ",
    '[f 4 4 3 0 1637]': "ぶつだはのねねぴぬつぱのゾ",
    '[f 4 4 3 0 1637]': "ぶつだはのねねぴぬつぱのタ",
    '[f 2 4 0]': "はつぱひのねだねだぬつねぴぬソ",
    '[f 2 4 1]': "はつぱひのねだねだぬつねぴぬゾ",
    '[f 2 4 2]': "っぬてソ",
    '[f 2 4 3]': "はつぱひのねだひなとににねぴぬソ",
}

# Reverse the fixed params dictionary for restoring original values
reverse_fixparamsindialog = {v: k for k, v in fixparamsindialog.items()}


def clean_dialogues(line):
    pattern_start = r'^\[[^\[\]]+\](?:\[[^\[\]]+\])*'
    pattern_end = r'(?:\[[^\[\]]+\])*$'
    clean_line = re.sub(pattern_start, '', line)
    clean_line = re.sub(pattern_end, '', clean_line)
    #
    clean_line = re.sub(r'\[n\]', ' ', clean_line)
    clean_line = re.sub(r'\[e\]', '', clean_line)
    clean_line = re.sub(r'\s+', ' ', clean_line).strip()
    for key, value in fixparamsindialog.items():
        clean_line = clean_line.replace(key, value)
    return clean_line


def restore_params(line):
    for key, value in reverse_fixparamsindialog.items():
        line = line.replace(key, value)
    return line

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


def process_input_file(input_path, max_length):
    output_filename = input_path

    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines[0] = lines[0].lstrip('\ufeff')

    clean_dialogues_list = []
    current_id = None
    current_dialogue = ""

    for line in lines:
        if line.startswith('[msg') or line.startswith('[sel'):
            if current_id:
                clean_dialogues_list.append((current_id, current_dialogue))
            current_id = line.strip()
            current_dialogue = ""
        else:
            max_len1, max_len2, type = max_length
            
            cleaned_line = clean_dialogues(line)
            transformed_line = set_n(cleaned_line, max_len1)
            
            if type == "normal":
                #logging.info(f"Normal se cumplió en {input_path}")
                if transformed_line.count('[n]') > 2:
                    #logging.info(f"Normal se cumplió en {input_path} y es mayor a 2")
                    transformed_line = ''.join(small_font.get(c, c) for c in cleaned_line)
                    transformed_line = set_n(transformed_line, max_len2)
            elif type == "top":
                #logging.info(f"Top se cumplió en {input_path}")
                if transformed_line.count('[n]') > 1:
                    #logging.info(f"Top se cumplió en {input_path} y es mayor a 1")
                    transformed_line = ''.join(small_font.get(c, c) for c in cleaned_line)
                    transformed_line = set_n(transformed_line, max_len2)
            
            current_dialogue += transformed_line + "\n"

    if current_id:
        clean_dialogues_list.append((current_id, current_dialogue))

    with open(output_filename, 'w', encoding='utf-8') as clean_file:
        for dialogue_id, dialogue in clean_dialogues_list:
            restored_params_dialogue = restore_params(dialogue)
            clean_file.write(f"{dialogue_id}\n{restored_params_dialogue}")


def determine_max_length(relative_path):
    if "battle\\event" in relative_path or "battle\\combination" in relative_path:
        return 40, 46, "normal"
    elif "event" in relative_path:
        return 40, 46, "normal"
    elif "battle" in relative_path:
        return 38, 44, "top"
    elif "camp" in relative_path:
        return 40, 46, "normal"
    elif "dungeon\\script\\support" in relative_path:
        return 38, 44, "top"
    elif "dungeon" in relative_path:
        return 40, 46, "normal"
    elif "facility\\townsupport.bmd.msg" in relative_path or "facility\\townsupport.msg" in relative_path:
        return 38, 44, "top"
    elif "facility" in relative_path:
        return 40, 46, "normal"
    elif "init\\dataQuestStory.bmd.msg" in relative_path or "init\\dataQuestStory.msg" in relative_path:
        return 40, 46, "normal"
    elif "init" in relative_path:
        return 40, 46, "normal"
    else:
        return 40, 46, "normal"


def process_all_files_in_directory(input_directory):
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith('.msg'):
                input_path = os.path.join(root, file)
                max_length = determine_max_length(input_path)

                process_input_file(input_path, max_length)

if __name__ == "__main__":
    logging.info("Processing Data directory")
    data_directory = "MsgEditorLT/Data"
    process_all_files_in_directory(data_directory)
    logging.info("Finished processing Data directory")
