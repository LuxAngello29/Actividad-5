# -*- coding: utf-8 -*-
"""ejercicio_5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11d4tKphHuJhUdwUcl0K5WprC5fjLwbSa
"""

def leer_archivo():
    ruta = "/content/archivo.txt"

    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print("❌ No se pudo leer el archivo. Archivo no encontrado.")
    except Exception as e:
        print(f"❌ Ocurrió un error al leer el archivo: {e}")


leer_archivo()

