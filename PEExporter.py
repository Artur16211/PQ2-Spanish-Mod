import os
import shutil
import subprocess

# Obtener la ruta al directorio del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa al ejecutable de PersonaEditor
persona_editor_path = os.path.join(
    script_dir, 'dependencies', 'PersonaEditor', 'PersonaEditorCMD.exe')


def run_peexport(input_path, output_dir):
    try:
        # Comprobar si la carpeta de salida ya existe, si no, crearla
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Mover el archivo al directorio de salida
        new_path = os.path.join(output_dir, os.path.basename(input_path))
        print(f"Moviendo '{input_path}' a '{new_path}'")
        shutil.move(input_path, new_path)

        # Construir el comando para ejecutar PersonaEditor
        command = f'"{persona_editor_path}" "{new_path}" -expall'
        print(f"Ejecutando: {command}")

        # Ejecutar el comando
        subprocess.run(command, check=True, shell=True)

        # Eliminar el archivo original después de la exportación
        os.remove(new_path)

    except Exception as e:
        print(f"Error al procesar {input_path}: {e}")
        # Intentar devolver el archivo si ocurrió un error después de moverlo
        if os.path.exists(new_path):
            shutil.move(new_path, input_path)


def process_directory(directory):
    print(f"Exportando...")
    # Recorrer el directorio y sus subdirectorios
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.bin', '.arc')):
                full_path = os.path.join(root, file)

                # Crear un directorio de salida para cada archivo específico manteniendo la extensión
                output_dir = os.path.join(root, file + '_dir')

                print(f"Creando directorio de salida: {output_dir}")
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                    # Construir la nueva ruta del archivo en el directorio de salida
                new_file_path = os.path.join(output_dir, file)

                # Mover el archivo al nuevo directorio
                shutil.move(full_path, new_file_path)

                # Aquí deberías llamar a `run_peexport` con el archivo ya en su nueva ubicación
                print(f"Procesando {new_file_path} en {output_dir}")
                run_peexport(new_file_path, output_dir)

    print(f"Creando directorios de subarchivos y moviendo archivos...")
    # Recorrer nuevamente para procesar los archivos exportados
    for root, dirs, files in os.walk(directory):
        for file in files:
            if '+' in file:
                # Obtener las partes de la ruta
                parts = file.split('+')
                # Crear la estructura de carpetas
                current_dir = root
                for folder_name in parts[:-1]:
                    current_dir = os.path.join(current_dir, folder_name)
                    if not os.path.exists(current_dir):
                        os.makedirs(current_dir)
                # Mover y renombrar el archivo
                # Usar todas las partes excepto la última (que es la extensión)
                print(f"Creando {current_dir}")
                new_folder_name = '.'.join(parts[:-1])
                new_file_path = os.path.join(current_dir, parts[-1])
                shutil.move(os.path.join(root, file), new_file_path)


def delete_files(directory):
    # Definir las extensiones de archivo a eliminar
    extensions_to_delete = ['.pm2', '.pm3', '.bed',
                            '.amd', '.tmp', '.track']

    for root, dirs, files in os.walk(directory):
        for file in files:
            # Convertir la extensión del archivo a minúsculas para comparar
            file_extension = os.path.splitext(file)[1].lower()
            # Verificar si la extensión está en la lista de extensiones a eliminar
            if file_extension in extensions_to_delete:
                # Eliminar el archivo
                os.remove(os.path.join(root, file))
                print(f"Eliminando {file}")


def eliminar_carpetas_vacias(root_directory):
    for root, dirs, files in os.walk(root_directory, topdown=False):
        for name in dirs:
            folder_path = os.path.join(root, name)
            if not os.listdir(folder_path):
                print(f"Eliminando carpeta vacía: {folder_path}")
                os.rmdir(folder_path)


if __name__ == "__main__":
    root_directory = "G:/SteamLibrary/steamapps/common/Persona 4 Golden/escpk"
    print(f"Procesando archivos en {root_directory}")
    process_directory(root_directory)
    print(f"Eliminando archivos innecesarios en {root_directory}")
    delete_files(root_directory)
    print(f"Eliminando carpetas vacías en {root_directory}")
    eliminar_carpetas_vacias(root_directory)
