import os


def remove_brackets(line):
    # Función para eliminar corchetes y su contenido de una línea
    while '[' in line:
        start = line.find('[')
        end = line.find(']')
        if start != -1 and end != -1:
            line = line[:start] + line[end + 1:]
    return line.strip()


def process_files(directory):
    duplicates = {}
    total_duplicates = 0  # Variable para almacenar el número total de líneas duplicadas
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.msg'):
                filepath = os.path.join(root, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    for line in file:
                        # Ignorar líneas que empiecen con '[msg'
                        if not line.startswith('[msg'):
                            processed_line = remove_brackets(line)
                            if processed_line:
                                if processed_line in duplicates:
                                    duplicates[processed_line].append(filepath)
                                    total_duplicates += 1
                                else:
                                    duplicates[processed_line] = [filepath]

    # Escribir líneas duplicadas en el archivo log
    with open('duplicates.log', 'w', encoding='utf-8') as log_file:
        for line, file_list in duplicates.items():
            if len(file_list) > 1:
                log_file.write(f"Line '{line}' is duplicated in:\n")
                for file in file_list:
                    log_file.write(f"- {file}\n")
                log_file.write('\n')

    print(f"Total duplicate lines found: {total_duplicates}")


if __name__ == "__main__":
    directory = r"C:\Users\Arthu\OneDrive\Escritorio\MSG_Q2\eng"
    process_files(directory)
