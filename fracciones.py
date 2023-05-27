def encontrar_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def simplificar(num, den):
    if den == 0:
        # genera una excepción manualmente
        raise ValueError("El denominador no puede ser cero.")
    mcd = encontrar_mcd(num, den)
    return num // mcd, den // mcd
# se crean listas para almacenar las fracciones y luego operar


def sumar(fracciones):
 #  En cada iteración suma acumulando de los numeradores multiplicados por los denominadores comunes
 # y actualiza el denominador común multiplicándolo por el denominador de la fracción actual.
    num_suma = 0
    den_comun = 1
    for fraccion in fracciones:
        num_suma = num_suma * fraccion[1] + fraccion[0] * den_comun
        den_comun *= fraccion[1]
    return simplificar(num_suma, den_comun)


def restar(fracciones):
    num_resta = 0
    den_comun = 1

    for fraccion in fracciones:
        num_resta = num_resta * fraccion[1] - fraccion[0] * den_comun
        den_comun *= fraccion[1]

    return simplificar(num_resta, den_comun)


def multiplicar(fracciones):
    num_prod = 1
    den_prod = 1
    for fraccion in fracciones:
        num_prod *= fraccion[0]
        den_prod *= fraccion[1]

    return simplificar(num_prod, den_prod)


def dividir(fracciones):
    num_div = fracciones[0][0] * fracciones[1][1]
    den_div = fracciones[0][1] * fracciones[1][0]

    return simplificar(num_div, den_div)


def ingresarFraccion():
    numerador = int(input("Ingrese el numerador de la fracción: "))
    denominador = int(input("Ingrese el denominador de la fracción: "))
    return numerador, denominador


def opciones(opcion):
    fracciones = []
# acá se inicia la lista vacia  de fracciones
    while opcion != "salir":
        if opcion == "suma" or opcion == "resta" or opcion == "multiplicacion" or opcion == "division":
         # verifica que se ingrese una opción válida
            try:
             # acá manejamos las expeciones, si todo es correcto se llama
             # a ingresar fracción para que el usuario ingrese un valor y se guarda en fracción
                fraccion = ingresarFraccion()
 # el metodo append ingresa una fraccion dentro de la lista vacia
                fracciones.append(fraccion)
 # si el valor es invalido se muestra un error, convierte error en un bloque de texto
            except ValueError as error:
                print("Error:", str(error))
        elif opcion == "salir":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            # realiza las operaciones y recibe la lista de fracciones para operar
        if opcion == "suma":
            resultado = sumar(fracciones)
            print(f"Resultado de la suma: {resultado[0]}/{resultado[1]}")
        elif opcion == "resta":
            resultado = restar(fracciones)
            print(f"Resultado de la resta: {resultado[0]}/{resultado[1]}")
        elif opcion == "multiplicacion":
            resultado = multiplicar(fracciones)
            print(
                f"Resultado de la multiplicación: {resultado[0]}/{resultado[1]}")
        elif opcion == "division":
            resultado = dividir(fracciones)
            print(f"Resultado de la división: {resultado[0]}/{resultado[1]}")

        opcion = input(
            "Ingrese una operación (suma, resta, multiplicacion, division) o 'salir' para terminar: ")


opcion = input(
    "Ingrese una operación (suma, resta, multiplicacion, division) o 'salir' para terminar: ")
opciones(opcion)
