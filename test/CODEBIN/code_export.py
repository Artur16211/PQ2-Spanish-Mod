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

def extract_content(file_path, offsets):
    contents = {}
    with open(file_path, 'rb') as file:
        for key, offset in offsets.items():
            file.seek(offset['start'])
            data = file.read(offset['end'] - offset['start'])
            text = ""
            for byte in data:
                if byte < 32 or byte > 126:
                    text += f"\\x{byte:02x}"
                else:
                    try:
                        text += byte.to_bytes(1, byteorder='big').decode('shift-jis')
                    except UnicodeDecodeError:
                        text += f"\\x{byte:02x}"
            contents[key] = text
    return contents

file_path = 'codeOG.bin'
contents = extract_content(file_path, offsets)

with open('extracted_content.txt', 'w', encoding='utf-8') as out_file:
    for key, content in contents.items():
        out_file.write(f"Offset {key}:\n{content}\n\n")

print("Extracción completada. El contenido ha sido guardado en 'extracted_content.txt'.")
