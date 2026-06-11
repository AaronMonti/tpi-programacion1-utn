import csv
import os

def leer_datos():
    lista = []
    ruta = "datos/paises_datos.csv"
    
    if not os.path.exists(ruta):
        return lista
        
    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo, delimiter=",")
        for line in lector:
            lista.append(line)
    return lista

def escribir_datos(datos, actualizar=False):
    columnas = ["nombre", "poblacion", "superficie", "continente"]
    modo_escritura = "w" if actualizar else "a"
    ruta = "datos/paises_datos.csv"
    
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    
    archivo_vacio = not os.path.exists(ruta) or os.path.getsize(ruta) == 0

    with open(ruta, modo_escritura, encoding="utf-8", newline="") as archivo:
        escritor_dict = csv.DictWriter(archivo, fieldnames=columnas)
        
        if actualizar or archivo_vacio:
            escritor_dict.writeheader()
            
        if actualizar:
            escritor_dict.writerows(datos)
        else:
            escritor_dict.writerow(datos)

def agregar_pais(datos):
    while True:
        try:
            nombre_pais = input("Ingrese el nombre del país: ").strip()
            if not nombre_pais:
                print("Error: El nombre del país no puede estar vacío.")
                continue
            poblacion = int(input("Ingrese la población: "))
            superficie = int(input("Ingrese la superficie: "))
            continente = input("Ingrese el continente: ").strip()
            if not continente:
                print("Error: El continente no puede estar vacío.")
                continue
            break
        except ValueError:
            print("Error: La población y la superficie deben ser números enteros.")    
            
    nuevo_pais = {"nombre": nombre_pais, "poblacion": str(poblacion), "superficie": str(superficie), "continente": continente}
    
    datos.append(nuevo_pais)
    escribir_datos(nuevo_pais, False)
    print(f"¡{nombre_pais} agregado con éxito!")

def actualizar_pais(datos):
    pais_buscado = input("Ingrese el nombre del país a actualizar: ").strip()
    encontrado = False

    for pais in datos:
        if pais["nombre"].lower() == pais_buscado.lower():
            encontrado = True
            # --- Validación población ---
            while True:
                try:
                    poblacion = int(input("Ingrese la nueva población: "))
                    break
                except ValueError:
                    print("Error: La población debe ser un número entero.")    
            
            # --- Validación superficie ---
            while True:
                try:
                    superficie = int(input("Ingrese la nueva superficie: "))
                    break
                except ValueError:
                    print("Error: La superficie debe ser un número entero.")
            
            # Modificamos los datos en la lista en memoria
            pais["poblacion"] = str(poblacion)
            box_superficie = pais["superficie"] = str(superficie)
            
            print(f"Datos actualizados en memoria: {pais}")
            break 
            
    if encontrado:
        escribir_datos(datos, True)
        print("¡Archivo CSV actualizado con éxito!")
    else:
        print("No se encontró el país.")

def buscar_pais(datos):
    pais_buscado = input("Ingrese el nombre del país a buscar: ").strip()

    coincidencias  = [pais for pais in datos if pais_buscado.lower() in pais["nombre"].lower()]

    if not coincidencias:
        print("No se encontraron coincidencias.")
        return

    if len(coincidencias) > 1:
        print("\nSe encontraron varios países:")
        for pais in coincidencias:
            print("País:", pais["nombre"], "| Continente:", pais["continente"], "| Población:", pais["poblacion"], "| Superficie:", pais["superficie"])
    else:
        pais_unico = coincidencias[0]
        print("\nPaís encontrado:")
        print("Nombre:", pais_unico["nombre"])
        print("Continente:", pais_unico["continente"])
        print("Población:", pais_unico["poblacion"])
        print("Superficie:", pais_unico["superficie"])

def filtrar_continente(datos):
    continente = input("Ingrese continente: ").strip()
    resultados = []
    for pais in datos:
        if pais["continente"].lower() == continente.lower():
            resultados.append(pais)
    if resultados:
        print("\nPaíses encontrados:")
        for pais in resultados:
            print(
                pais["nombre"],
                pais["poblacion"],
                pais["superficie"],
                pais["continente"]
            )
    else:
        print("No se encontraron países.")

def menu_filtros(datos):
    print("\n--- FILTROS ---")
    print("1. Continente")
    print("2. Rango de población")
    print("3. Rango de superficie")

    opcion = int(input("Seleccione: "))
    if opcion == 1:
        filtrar_continente(datos)
    elif opcion == 2:
        filtrar_poblacion(datos)
    elif opcion == 3:
        filtrar_superficie(datos)
    else:
        print("Opción inválida")

def filtrar_poblacion(datos):
    minimo = int(input("Población mínima: "))
    maximo = int(input("Población máxima: "))
    encontrados = []
    for pais in datos:
        poblacion = int(pais["poblacion"])
        if minimo <= poblacion <= maximo:
            encontrados.append(pais)
    if encontrados:
        for pais in encontrados:
            print(
                pais["nombre"],
                pais["poblacion"]
            )
    else:
        print("Sin resultados.")

def filtrar_superficie(datos):
    minimo = int(input("Superficie mínima: "))
    maximo = int(input("Superficie máxima: "))
    encontrados = []
    for pais in datos:
        superficie = int(pais["superficie"])
        if minimo <= superficie <= maximo:
            encontrados.append(pais)
    if encontrados:
        for pais in encontrados:
            print(
                pais["nombre"],
                pais["superficie"]
            )
    else:
        print("Sin resultados.")

def ordenar_nombre(datos):
    ordenados = sorted(
        datos,
        key=lambda pais: pais["nombre"]
    )
    for pais in ordenados:
        print(pais["nombre"])

def ordenar_poblacion(datos):
    ordenados = sorted(
        datos,
        key=lambda pais: int(pais["poblacion"])
    )
    for pais in ordenados:
        print(
            pais["nombre"],
            pais["poblacion"]
        )

def ordenar_superficie(datos):
    opcion = input(
        "Ascendente(A) o Descendente(D): "
    ).upper()
    reverse = opcion == "D"
    ordenados = sorted(
        datos,
        key=lambda pais: int(pais["superficie"]),
        reverse=reverse
    )
    for pais in ordenados:
        print(
            pais["nombre"],
            pais["superficie"]
        )
def menu_ordenamientos(datos):
    print("\n--- ORDENAR ---")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

    opcion = int(input("Seleccione: "))
    if opcion == 1:
        ordenar_nombre(datos)
    elif opcion == 2:
        ordenar_poblacion(datos)
    elif opcion == 3:
        ordenar_superficie(datos)
    else:
        print("Opción inválida")

def mostrar_estadisticas(datos):
    mayor = max(
        datos,
        key=lambda pais: int(pais["poblacion"])
    )

    menor = min(
        datos,
        key=lambda pais: int(pais["poblacion"])
    )

    promedio_poblacion = sum(
        int(pais["poblacion"])
        for pais in datos
    ) / len(datos)

    promedio_superficie = sum(
        int(pais["superficie"])
        for pais in datos
    ) / len(datos)

    continentes = {}

    for pais in datos:
        continente = pais["continente"]
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\n--- ESTADÍSTICAS ---")
    print(
        f"Mayor población: {mayor['nombre']} ({mayor['poblacion']})"
    )
    print(
        f"Menor población: {menor['nombre']} ({menor['poblacion']})"
    )
    print(
        f"Promedio población: {promedio_poblacion:.2f}"
    )
    print(
        f"Promedio superficie: {promedio_superficie:.2f}"
    )
    print("\nCantidad por continente:")
    for continente, cantidad in continentes.items():
        print(
            continente,
            ":",
            cantidad
        )

def menu():
    # Cargamos los datos una sola vez al iniciar el programa
    datos = leer_datos()

    while True:
        print("\n--- MENU ---")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Estadísticas")
        print("7. Salir")
        
        try:
            opcion = int(input("Elegí una opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if opcion == 1:
            agregar_pais(datos)
        elif opcion == 2:
            actualizar_pais(datos)
        elif opcion == 3:
            buscar_pais(datos)
        elif opcion == 4:
            menu_filtros(datos)
        elif opcion == 5:
            menu_ordenamientos(datos)
        elif opcion == 6:
            mostrar_estadisticas(datos)
        elif opcion == 7:
            print("Finalizando sistema.")
            break
        else:
            print("Opción incorrecta. Intenta de nuevo.")

if __name__ == "__main__":
    menu()