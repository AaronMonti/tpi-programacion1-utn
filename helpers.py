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