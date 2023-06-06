# def suma_clasica():
#     cantidad_numeros = int(input("Ingrese la cantidad de números a sumar: "))
#     resultado = 0
#     for i in range(cantidad_numeros):
#         numero = int(input("Ingrese el número: "))
#         resultado += numero
#     print("La suma es:", resultado)

# def resta_clasica():
#     cantidad_numeros = int(input("Ingrese la cantidad de números a restar: "))
#     resultado = int(input("Ingrese el primer número: "))
#     for i in range(1, cantidad_numeros):
#         numero = int(input("Ingrese el número: "))
#         resultado -= numero
#     print("La resta es:", res ultado)

# def multiplicacion_clasica():
#     cantidad_numeros = int(input("Ingrese la cantidad de números a multiplicar: "))
#     resultado = 1
#     for i in range(cantidad_numeros):
#         numero = int(input("Ingrese el número: "))
#         resultado *= numero
#     print("La multiplicación es:", resultado)

# def division_clasica():
#     cantidad_numeros = int(input("Ingrese la cantidad de números a dividir: "))
#     resultado = int(input("Ingrese el primer número: "))
#     for i in range(1, cantidad_numeros):
#         numero = int(input("Ingrese el número: "))
#         if numero == 0:
#             print("Error: no se puede dividir por cero.")
#             return
#         resultado /= numero
#     print("La división es:", resultado)

# funcion = int(input("ingrese 1: "))
# if funcion == 1:
#     operacion = str(input("ingrese tipo de operacion (sum para suma, res para resta, mul para multiplicacion, div para division): "))
#     if operacion == "sum":
#         suma_clasica()
#         print("resultado es: " , suma_clasica())
#     elif operacion == "res":
#         resta_clasica()
#         print("resultado es: " , resta_clasica())


#     elif operacion == "mul":
#         multiplicacion_clasica()
#         print("resultado es: " , multiplicacion_clasica())


#     elif operacion == "div":
#         division_clasica()
#         print("resultado es: " , division_clasica())

#variable para iniciar
prender = str(input("ingrese 'on' para iniciar: "))
def suma():
    total_suma = 0
    for num in lista_funcion_clasica:
        total_suma += num
    resultado_final_sum = str(input("ingresar = para imprimir resultado: "))
    if resultado_final_sum == "=":
        print("total de suma es:", total_suma)
def resta():
    if len(lista_funcion_clasica) > 0:
        total_resta = lista_funcion_clasica[0]
        for num in lista_funcion_clasica[1:]:
            total_resta -= num
                #imprime resultado final
        resultado_final_resta = str(input("ingresar = para imprimir resultado: "))
        if resultado_final_resta == "=":
            print("total de resta es:", total_resta)
    else:
        print("lista vacia")


#inicia la calculadora
while prender == "on":
    funcion = int(input("ingresar tipo de calculadora desea utilizar (1 clasica, 2 fracciones, 3 conversion, 4 para salir (off)): "))
    #funcion calculadora clasica
    if funcion == 1:
        #lista donde se guardan los numeros ingresados
        lista_funcion_clasica = []
        #ingreso numeros
        numeros_funcion_clasica = float(input("ingresar numero (o 0 para terminar): "))
        while numeros_funcion_clasica != 0:
            #se agregan los numeros a la lista
            lista_funcion_clasica.append(numeros_funcion_clasica)
            numeros_funcion_clasica = float(input("ingresar numero (o 0 para terminar): "))
        #ingreso el tipo de cuenta
        cuenta = input("ingresar tipo de cuenta (SUM para suma, RES para resta, MUL para multiplicacion, DIV para division): ")
        #suma
        if cuenta == "SUM":
            suma()
        #resta
        elif cuenta == "RES":
            resta()
        #multiplicacion
        elif cuenta == "MUL":
            if len(lista_funcion_clasica) > 0:
                total_multiplicacion = 1
                for num in lista_funcion_clasica:
                    total_multiplicacion *= num
                #imprime resultado final
                resultado_final_multiplicacion = str(input("ingresar = para imprimir resultado: "))
                if resultado_final_multiplicacion == "=":
                    print("total de multiplicación es:", total_multiplicacion)
            else:
                print("lista vacia")

        elif cuenta == "DIV":
            if len(lista_funcion_clasica) > 0:
                total_division = lista_funcion_clasica[0]
                for num in lista_funcion_clasica[1:]:
                    if num != 0:
                        total_division /= num
                    else:
                        print("No se puede dividir por cero.")
                        break

                resultado_final_division = str(input("ingresar = para imprimir resultado: "))
                if resultado_final_division == "=":
                    print("total de division es:", total_division)
            else:
                print("error")
