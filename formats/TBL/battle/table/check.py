import re

special_chars = "↓※〒ホボポマミレロヮワヰムメ"

combined_pattern = f"ｶ[{re.escape(special_chars)}]"

def count_characters(line):
    line_normalized = re.sub(combined_pattern, "X", line)
    line_normalized = re.sub(f"[{re.escape(special_chars)}]", " ", line_normalized)
    return len(line_normalized)

def filter_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if count_characters(line) > 17:
                print(line, end='')

filter_lines('skillnametable.ebl')
