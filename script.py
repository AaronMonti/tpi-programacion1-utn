import csv

# Obtencion de datos en una lista (cada país es un dict dentro de la lista)
def datos():
    list = []
    with open("datos/paises_datos.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for line in lector:
            list.append(line)
    
    return list

# Menu modular, recibe opciones con sus respectivas funciones como param
def menu(opciones):
    salir_programa = False

    while not salir_programa:
        print("\n--- MENU ---")
        
        for i, (texto, _) in enumerate(opciones, start=1):
            print(f"{i}. {texto}")

        try:
            eleccion = int(input("Elegí una opción: "))
            _, funcion = opciones[eleccion - 1]

            resultado = funcion()

            if resultado is True:
                salir_programa = True

        except (ValueError, IndexError):
            print("Opción inválida")

def menu_filtros():
    menu(opciones_filtros)

def menu_ordenamientos():
    menu(opciones_ordenamientos)

def menu_principal():
    menu(opciones_principales)

def texto_prueba():
    print("Prueba")

# Opciones del menu de filtros
opciones_filtros = [
    ("Continente", texto_prueba),
    ("Rango de población", texto_prueba),
    ("Rango de superficie", texto_prueba),
    ("Volver", menu_principal),
]

# Opciones del menu de ordenamientos
opciones_ordenamientos = [
    ("Nombre", texto_prueba),
    ("Poblacion", texto_prueba),
    ("Superficie (ascendente o descendente)", texto_prueba),
    ("Volver", menu_principal),
]

# Opciones del menu principal
opciones_principales = [
    ("Agregar país", texto_prueba),
    ("Actualizar población y superficie", texto_prueba),
    ("Buscar un país", texto_prueba),
    ("Filtrar países", menu_filtros),
    ("Ordenar países", menu_filtros),
    ("Mostrar estadisticas", texto_prueba),
    ("Salir", texto_prueba),
]

menu(opciones_principales)