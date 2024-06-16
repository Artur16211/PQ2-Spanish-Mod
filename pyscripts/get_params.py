import re

def only_params(text):
    pattern = r'(?<=\])([^[]+)(?=\[|$)'
    modified_text = re.sub(pattern, r'{dialog}', text)

    # Eliminar '{dialog}' al final del texto
    modified_text = re.sub(r'\{dialog\}$', '', modified_text)

    # Eliminar '{dialog}' excepto el último
    final_text = re.sub(r'\{dialog\}.*\{dialog\}', '{dialog}', modified_text)
    
    return final_text

# text = "[f 0 5 65278][f 2 1][f 4 6 19 2 2 0][f 1 5][f 6 1 27 0 0 0][n][f 3 1 1 0 0 19031]I was so focused on rescuing everyone[n]that I really went overboard on those[n]Shadows back there.[n][f 1 3 65535][f 1 1][e]"
# print(only_params(text))