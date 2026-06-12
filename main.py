from helpers import imprimir_error
from datos import leer_datos
from funcionalidades import (
    agregar_pais,
    actualizar_pais,
    buscar_pais,
    filtrar_paises,
    menu_ordenamientos,
    mostrar_estadisticas,
)


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
            filtrar_paises(datos)
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