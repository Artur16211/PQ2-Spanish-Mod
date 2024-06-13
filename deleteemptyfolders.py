import os


def eliminar_carpetas_vacias(root_directory):
    for root, dirs, files in os.walk(root_directory, topdown=False):
        for name in dirs:
            folder_path = os.path.join(root, name)
            if not os.listdir(folder_path):
                print(f"Eliminando carpeta vacía: {folder_path}")
                os.rmdir(folder_path)


if __name__ == "__main__":
    # root_directory = "G:/Q2/Programs/Aemulus/Packages/Persona 4 Golden/SpanishTest/data_e"
    root_directory = "C:/Users/Artur/Desktop/P4G64ModsES/p4gpc.animemusicexpansionES/P5REssentials/CPK/data/event"
    print(f"Eliminando carpetas vacías en {root_directory}")
    eliminar_carpetas_vacias(root_directory)
