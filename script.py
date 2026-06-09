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

def menu():
    # Cargamos los datos una sola vez al iniciar el programa
    datos = leer_datos()

    while True:
        print("\n--- MENU ---")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Salir")
        
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
            print("¡Hasta luego!")
            break
        else:
            print("Opción incorrecta. Intenta de nuevo.")

if __name__ == "__main__":
    menu()