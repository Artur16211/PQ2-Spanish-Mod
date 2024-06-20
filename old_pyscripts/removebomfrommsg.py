import os

def remove_utf8_bom(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
    if content.startswith(b'\xef\xbb\xbf'):
        content = content[3:]  # Remove the BOM
        with open(file_path, 'wb') as file:
            file.write(content)
        print(f'Removed BOM from: {file_path}')
    else:
        print(f'No BOM found in: {file_path}')

def convert_files_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.msg'):
                file_path = os.path.join(root, file)
                remove_utf8_bom(file_path)

if __name__ == "__main__":
    directory = input("Enter the directory containing .msg files: ")
    convert_files_in_directory(directory)
