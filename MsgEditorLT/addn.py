import re


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
