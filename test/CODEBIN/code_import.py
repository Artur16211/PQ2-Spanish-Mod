import shutil

def convert_to_binary(text):
    binary_data = bytearray()
    i = 0
    while i < len(text):
        if text[i] == '\\' and text[i+1] == 'x':
            # Convert hexadecimal sequence to byte
            hex_value = text[i+2:i+4]
            binary_data.append(int(hex_value, 16))
            i += 4
        else:
            # Convert character to bytes using shift-jis encoding
            char = text[i]
            binary_data.extend(char.encode('shift-jis'))
            i += 1
    return binary_data

def reimport_content(original_file_path, new_file_path, offsets, modified_contents):
    shutil.copyfile(original_file_path, new_file_path)

    with open(new_file_path, 'r+b') as file:
        for key, offset in offsets.items():
            if key in modified_contents:
                binary_data = convert_to_binary(modified_contents[key])
                file.seek(offset['start'])
                file.write(binary_data)

original_file_path = 'code.bin'
new_file_path = 'code_mod.bin'

offsets = {
    "0": {"start": 0x4364DB, "end": 0x436758},
    "1": {"start": 0x48BE1A, "end": 0x48DCB3},
    "3": {"start": 0x42D254, "end": 0x42D509},
    "4": {"start": 0x435F0F, "end": 0x436127},
    "5": {"start": 0x43617C, "end": 0x4362BB},
    "6": {"start": 0x42BC20, "end": 0x42BD07},
    "8": {"start": 0x431C3C, "end": 0x431D3F},
    "9": {"start": 0x431D90, "end": 0x431E4E},
    "10": {"start": 0x435F40, "end": 0x436127},
}
modified_contents = {}
with open('modified_content.txt', 'r', encoding='utf-8') as in_file:
    current_key = None
    content = ""
    for line in in_file:
        if line.startswith("Offset"):
            if current_key is not None:
                modified_contents[current_key] = content
            current_key = line.split()[1].strip(':')
            content = ""
        else:
            content += line.strip()
    if current_key is not None:
        modified_contents[current_key] = content

reimport_content(original_file_path, new_file_path, offsets, modified_contents)

print("Reimportación completada. El archivo modificado ha sido guardado como 'code_mod.bin'.")