def eliminar_lineas_vacias(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo_original:
            lineas = archivo_original.readlines()
        
        # Filtrar las líneas no vacías
        lineas_filtradas = [linea for linea in lineas if linea.strip() != '']
        
        with open(nombre_archivo, 'w') as archivo_modificado:
            archivo_modificado.writelines(lineas_filtradas)
        
        print(f'Se eliminaron las líneas vacías en el archivo "{nombre_archivo}".')

    except FileNotFoundError:
        print(f'No se encontró el archivo "{nombre_archivo}".')

# Ejemplo de uso
archivo = 'q1entbl.txt'  # Reemplaza con el nombre de tu archivo
eliminar_lineas_vacias(archivo)
