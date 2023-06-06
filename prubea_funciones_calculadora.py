lista_funcion_clasica = []
#funcion calculadora clasica
def fun_clasica():
    global lista_funcion_clasica
        #ingreso numeros
    numeros_funcion_clasica = float(input("ingresar numero (o 0 para terminar): "))
    while numeros_funcion_clasica != 0:
            #se agregan los numeros a la lista
        lista_funcion_clasica.append(numeros_funcion_clasica)
        numeros_funcion_clasica = float(input("ingresar numero (o 0 para terminar): "))

        #funcion suma de calculadora clasica
def sum_clasica():
    global lista_funcion_clasica
    total_suma = 0
    for num in lista_funcion_clasica:
        total_suma += num
            #imprime resultado final
    resultado_final_sum = str(input("ingresar = para imprimir resultado: "))
    if resultado_final_sum == "=":
        print("total de suma es:", total_suma)
    else:
        print("error")
    lista_funcion_clasica.clear()

        #funcion resta de calculadora clasica
def res_clasica():
    global lista_funcion_clasica
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
    lista_funcion_clasica.clear()

        #funcion multiplicacion de calculadora clasica
def mul_clasica():
    global lista_funcion_clasica
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
    lista_funcion_clasica.clear()

        #funcion division de calculadora clasica
def div_clasica():
    global lista_funcion_clasica
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
        lista_funcion_clasica.clear()
#variable para iniciar
prender = str(input("ingrese 'on' para iniciar: "))
#inicia la calculadora
while prender == "on":
    funcion = int(input("ingresar tipo de calculadora desea utilizar (1 clasica, 2 fracciones, 3 conversion, 4 para salir (off)): "))

    if funcion == 1:
        fun_clasica()
        cuenta = input("ingresar tipo de cuenta (SUM para suma, RES para resta, MUL para multiplicacion, DIV para division): ")
        if cuenta == "SUM":
             sum_clasica()
        elif cuenta == "RES":
            res_clasica()
        elif cuenta == "MUL":
            mul_clasica()
            


        
