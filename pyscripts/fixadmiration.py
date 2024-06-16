import os
import re

def corregir_frase(frase):
    patron = re.compile(r'夷([^夷!\?]*?)!')

    nueva_frase = patron.sub(r'斡\1!', frase)

    return nueva_frase

def procesar_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        lineas_corregidas = [corregir_frase(linea) for linea in lineas]

        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            for linea_corregida in lineas_corregidas:
                archivo.write(linea_corregida)

    except Exception as e:
        print(f"No se pudo corregir el archivo {ruta_archivo}: {e}")


def procesar_directorio(ruta_directorio):
    for raiz, directorios, archivos in os.walk(ruta_directorio):
        for archivo in archivos:
            if archivo.endswith('.msg'):
                ruta_archivo = os.path.join(raiz, archivo)
                procesar_archivo(ruta_archivo)


root_dir = 'C:/Users/Artur/Documents/Q2_SETNV2/setn_test/_Q2ESP'
procesar_directorio(root_dir)
