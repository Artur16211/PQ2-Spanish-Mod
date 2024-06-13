import os


def rename_to_lowercase(directory):
    # Recorrer el directorio y sus subdirectorios
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Construir la ruta completa al archivo
            old_file_path = os.path.join(root, file)
            # Construir el nuevo nombre de archivo en minúsculas
            new_file_name = file.lower()
            new_file_path = os.path.join(root, new_file_name)
            # Renombrar el archivo si el nombre actual no está en minúsculas
            if file != new_file_name:
                os.rename(old_file_path, new_file_path)
                print(f"Renombrando {file} a {new_file_name}")


if __name__ == "__main__":
    # Define la carpeta raíz para empezar a procesar
    root_directory = "G:/Q2/Programs/Aemulus/Packages/Persona 4 Golden/SpanishTest/data_e"
    print(f"Renombrando archivos en {root_directory} a minúsculas")
    rename_to_lowercase(root_directory)
