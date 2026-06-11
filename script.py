import csv
import os

# HELPERS

def imprimir_exito(mensaje):
    print(f"✔ {mensaje}\n")
 
def imprimir_error(mensaje):
    print(f"❌ {mensaje}\n")
 
def imprimir_aviso(mensaje):
    print(f"❕ {mensaje}\n")

def pedir_texto(mensaje, campo="campo"):
    """Pide un texto no vacío al usuario."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        imprimir_error(f"{campo.title()} no puede estar vacío.")
 
def pedir_entero_positivo(mensaje, campo="valor"):
    """Pide un entero positivo al usuario."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                imprimir_error(f"{campo.title()} debe ser un número positivo.")
                continue
            return valor
        except ValueError:
            imprimir_error(f"{campo.title()} debe ser un número entero.")

def pedir_rango(campo):
    """Pide un rango mínimo/máximo válido. Devuelve (min, max)."""
    while True:
        minimo = pedir_entero_positivo(f"  Ingrese el mínimo de {campo}: ", campo)
        maximo = pedir_entero_positivo(f"  Ingrese el máximo de {campo}: ", campo)
        if minimo > maximo:
            imprimir_error("El mínimo no puede ser mayor que el máximo.")
            continue
        return minimo, maximo

# DATOS

def leer_datos():
    """Lee el CSV y devuelve una lista de diccionarios."""

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
    """
    Escribe datos en el CSV.
    - actualizar=True  → sobreescribe todo el archivo (usado al actualizar un país).
    - actualizar=False → agrega una fila al final (usado al agregar un país).
    """

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

# FUNCIONALIDADES

def agregar_pais(datos):
    nombre_pais = pedir_texto("Ingrese el nombre del país: ", "nombre")
    
    if any(p["nombre"].lower() == nombre_pais.lower() for p in datos):
        imprimir_error(f"Ya existe un país con el nombre '{nombre_pais}'.")
        return
    poblacion = pedir_entero_positivo("Ingrese la población: ", "poblacion")
    superficie = pedir_entero_positivo("Ingrese la superficie: ", "superficie")
    continente = pedir_texto("Ingrese el continente: ", "continente")
    nuevo_pais = {
        "nombre": nombre_pais,
        "poblacion": str(poblacion),
        "superficie": str(superficie),
        "continente": continente
    }
    
    datos.append(nuevo_pais)
    escribir_datos(nuevo_pais, actualizar=False)
    imprimir_exito(f"{nombre_pais} agregado con éxito.")

def actualizar_pais(datos):
    if not datos:
        imprimir_aviso("No hay países cargados.")
        return

    pais_buscado = pedir_texto("Ingrese el nombre del país a actualizar: ", "nombre")
    encontrado = False

    for pais in datos:
        if pais["nombre"].lower() == pais_buscado.lower():
            encontrado = True

            poblacion = pedir_entero_positivo("Ingrese la nueva población: ", "poblacion")
            superficie = pedir_entero_positivo("Ingrese la nueva superficie: ", "superficie")
            
            # Modificamos los datos en la lista en memoria
            pais["poblacion"] = str(poblacion)
            pais["superficie"] = str(superficie)
            
    if encontrado:
        escribir_datos(datos, actualizar=True)
        imprimir_exito(f"{pais_buscado} actualizado con éxito.")
    else:
        imprimir_error(f"No se encontró ningun país con el nombre '{pais_buscado}'.")

def buscar_pais(datos):
    if not datos:
        imprimir_aviso("No hay países cargados.")
        return

    pais_buscado = pedir_texto("Ingrese el nombre del país a buscar: ", "nombre")

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
def filtrar_continente(datos):
    set_continentes = set()
    for pais in datos:
        set_continentes.add(pais["continente"])
    continentes = list(set_continentes)

    while True:
        print("\n--- CONTINENTES DISPONIBLES ---")
        
        for i, nombre in enumerate(continentes, start=1):
            print(f"{i}. {nombre}")
        
        while True:
            try:
                opcion = int(input("Elegí una opción: "))
                if 1 <= opcion <= len(continentes):
                    continente_elegido = continentes[opcion - 1]
                    break
                imprimir_error(f"Opcion fuera de rango. Ingrese un número entre 1 y {len(continentes)}")
            except ValueError:
                imprimir_error("Por favor, ingrese un número válido.")

        coincidencias  = [pais for pais in datos if continente_elegido.lower() in pais["continente"].lower()]
        for pais in coincidencias:
            print("País:", pais["nombre"], "| Continente:", pais["continente"], "| Población:", pais["poblacion"], "| Superficie:", pais["superficie"])
        break

def filtrar_por_rango(datos, tipo):
    min, max = pedir_rango(tipo)
    print("Rango de población")

    if tipo == "poblacion":
        coincidencias = [pais for pais in datos if min < int(pais["poblacion"]) < max]
    elif tipo == "superficie":
        coincidencias = [pais for pais in datos if min < int(pais["superficie"]) < max]
    print(f"Países con {tipo} entre {min} y {max}")
    for pais in coincidencias:
        print("País:", pais["nombre"], "| Continente:", pais["continente"], "| Población:", pais["poblacion"], "| Superficie:", pais["superficie"])



def filtrar_paises(datos):
    while True:
        print("\n--- FILTROS ---")
        print("1. Por continente")
        print("2. Rango de poblacion")
        print("3. Rango de superficie")
        print("4. Volver")
        
        try:
            opcion = int(input("Elegi una opción: "))
        except ValueError:
            imprimir_error("Por favor, ingresa un número válido.")
            continue

        if opcion == 1:
            filtrar_continente(datos)
            break
        elif opcion == 2:
            filtrar_por_rango(datos, tipo="poblacion")
            break
        elif opcion == 3:
            filtrar_por_rango(datos, tipo="superficie")
            break
        elif opcion == 4:
            break
        else:
            imprimir_error("Opción incorrecta. Intente de nuevo.")

def menu():
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
            imprimir_error("Por favor, ingresa un número válido.")
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