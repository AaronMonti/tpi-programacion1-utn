import csv
from helpers import imprimir_error

RUTA_ARCHIVO = "datos/paises_datos.csv"

def leer_datos():
    """Lee el CSV y devuelve una lista de diccionarios."""

    lista = []

    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, delimiter=",")
            for line in lector:
                lista.append(line)
    except FileNotFoundError:
        imprimir_error(f"El archivo '{RUTA_ARCHIVO}' no se encontró en la carpeta")

    return lista

def escribir_datos(datos, actualizar=False):
    """
    Escribe datos en el CSV.
    - actualizar=True  → sobreescribe todo el archivo (usado al actualizar un país).
    - actualizar=False → agrega una fila al final (usado al agregar un país).
    """

    columnas = ["nombre", "poblacion", "superficie", "continente"]
    modo_escritura = "w" if actualizar else "a"

    try:
        with open(RUTA_ARCHIVO, modo_escritura, encoding="utf-8", newline="") as archivo:
            escritor_dict = csv.DictWriter(archivo, fieldnames=columnas)

            if actualizar:
                escritor_dict.writeheader()

            if actualizar:
                escritor_dict.writerows(datos)
            else:
                escritor_dict.writerow(datos)
    except FileNotFoundError:
        imprimir_error(f"El archivo '{RUTA_ARCHIVO}' no se encontró en la carpeta")