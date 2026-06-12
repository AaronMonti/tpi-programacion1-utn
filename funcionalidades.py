from helpers import (
    imprimir_exito,
    imprimir_error,
    imprimir_aviso,
    pedir_texto,
    pedir_entero_positivo,
    pedir_rango,
)
from datos import escribir_datos


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

    coincidencias = [pais for pais in datos if pais_buscado.lower() in pais["nombre"].lower()]

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
    if not datos:
        imprimir_aviso("No hay países cargados.")
        return
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

        coincidencias = [pais for pais in datos if continente_elegido.lower() in pais["continente"].lower()]
        for pais in coincidencias:
            print("País:", pais["nombre"], "| Continente:", pais["continente"], "| Población:", pais["poblacion"], "| Superficie:", pais["superficie"])
        break


def filtrar_por_rango(datos, tipo):
    if not datos:
        imprimir_aviso("No hay países cargados.")
        return
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
    if not datos:
        imprimir_aviso("No hay países cargados.")
        return
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


def ordenar_nombre(datos):
    if not datos:
        imprimir_aviso("No hay países cargados.")
        return
    ordenados = sorted(
        datos,
        key=lambda pais: pais["nombre"]
    )
    for pais in ordenados:
        print("País:", pais["nombre"], "| Continente:", pais["continente"], "| Población:", pais["poblacion"], "| Superficie:", pais["superficie"])


def ordenar_poblacion(datos):
    if not datos:
        imprimir_aviso("No hay países cargados.")
        return
    ordenados = sorted(
        datos,
        key=lambda pais: int(pais["poblacion"])
    )
    for pais in ordenados:
        print("País:", pais["nombre"], "| Continente:", pais["continente"], "| Población:", pais["poblacion"], "| Superficie:", pais["superficie"])


def ordenar_superficie(datos):
    if not datos:
        imprimir_aviso("No hay países cargados.")
        return
    opcion = input(
        "Ascendente(A) o Descendente(D): "
    ).upper()
    while opcion != "A" and opcion != "D":
        imprimir_error("Por favor, ingresa un número válido.")
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
        print("País:", pais["nombre"], "| Continente:", pais["continente"], "| Población:", pais["poblacion"], "| Superficie:", pais["superficie"])


def menu_ordenamientos(datos):
    if not datos:
        imprimir_aviso("No hay países cargados.")
        return
    print("\n--- ORDENAR ---")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

    try:
        opcion = int(input("Elegí una opción: "))
    except ValueError:
        imprimir_error("Por favor, ingresa un número válido.")
        return

    if opcion == 1:
        ordenar_nombre(datos)
    elif opcion == 2:
        ordenar_poblacion(datos)
    elif opcion == 3:
        ordenar_superficie(datos)
    else:
        imprimir_error("Opción inválida")


def mostrar_estadisticas(datos):
    if not datos:
        imprimir_aviso("No hay países cargados.")
        return
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