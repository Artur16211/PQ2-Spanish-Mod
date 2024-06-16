import os
import re

def corregir_frase(frase):
    # Expresión regular para encontrar el patrón "夷...!" sin signo de interrogación de cierre intermedio
    patron = re.compile(r'夷([^夷!\?]*?)!')

    # Reemplazar "夷" por "斡" donde se encuentre el patrón
    nueva_frase = patron.sub(r'斡\1!', frase)

    return nueva_frase

def procesar_archivo(ruta_archivo):
    try:
        # Abrir el archivo y leer su contenido línea por línea
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        # Corregir cada línea del archivo
        lineas_corregidas = [corregir_frase(linea) for linea in lineas]

        # Escribir las líneas corregidas de vuelta al archivo
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            for linea_corregida in lineas_corregidas:
                archivo.write(linea_corregida)

        #print(f"Archivo {ruta_archivo} corregido con éxito.")
    except Exception as e:
        print(f"No se pudo corregir el archivo {ruta_archivo}: {e}")


def procesar_directorio(ruta_directorio):
    for raiz, directorios, archivos in os.walk(ruta_directorio):
        for archivo in archivos:
            if archivo.endswith('.msg'):  # Puedes ajustar la extensión de archivo según tus necesidades
                ruta_archivo = os.path.join(raiz, archivo)
                procesar_archivo(ruta_archivo)


# Ruta del directorio raíz donde se encuentran los archivos
root_dir = 'C:/Users/Artur/Documents/Q2_SETNV2/setn_test/_Q2ESP'
procesar_directorio(root_dir)
