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



#<--------------------------------------><-------------------------------------------------------->


#funcion calculadora de fracciones
def cal_fracciones():
    numerador = int(input("ingrese numerador: "))
        #ingresa primer denominador
    denominador = int(input("ingrese denominador: "))
        #error si denominador es igual a 0
    if denominador == 0:
            print("Ingrese un denominador distinto de 0")
        #ingresa segundo numerador
    numerador_2 = int(input("ingrese numerador de la segunda fraccion: "))
        #ingresa segundo denominador
    denominador_2 = int(input("ingrese denominador de la segunda fraccion: "))
        #error si denominador es igual a 0
    if denominador_2 == 0:
            print("Ingrese un denominador distinto de 0")
        #tipo de cuenta que se ingresa
    cuenta = input("ingresar tipo de cuenta (SUM para suma, RES para resta, MUL para multiplicacion, DIV para division): ")
        #suma
    if cuenta == "SUM":
            #se busca denominador comun
        den_comun = denominador * denominador_2
        print("El denominador común sería:", den_comun)
            #se busca el primer numerador
        num_comun_1 = numerador * denominador_2
        print("El primer numerador es:", num_comun_1)
            #se busca el segundo numerador
        num_comun_2 = numerador_2 * denominador
        print("El segundo numerador es:", num_comun_2)
            #se suman los dos numeradores
        suma_num = num_comun_1 + num_comun_2
        print("la cuenta quedaria tal que asi: " , num_comun_1, "+" , num_comun_2 , "sobre" , den_comun)
            #ingresar = para imprimir el resultado final
        resultado_final = input("ingrese = para resultado final: ")
        if resultado_final == "=":
                #imprime resultado final
                print("El resultado es:",suma_num,"/",den_comun)
        #resta
    elif cuenta == "RES":
            #se busca denominador comun
        den_comun = denominador * denominador_2
        print("El denominador común sería:", den_comun)
            #se busca el primer numerador
        num_comun_1 = numerador * denominador_2
        print("El primer numerador es:", num_comun_1)
            #se busca el segundo numerador
        num_comun_2 = numerador_2 * denominador
        print("El segundo numerador es:", num_comun_2)
            #la resta de los numeradores
        resta_num = num_comun_1 - num_comun_2
        print("la cuenta quedaria tal que asi: ", num_comun_1 , "-" , num_comun_2 , "sobre" , den_comun )
            #ingresar = para imprimir el resultado final
        resultado_final = input("ingrese = para resultado final: ")
        if resultado_final == "=":
                #imprime resultado final
            print("El resultado es:",resta_num,"/",den_comun)
        #multiplicacion
    elif cuenta == "MUL":
            #numeroador
        numerador_final = numerador * numerador_2
            #denominador
        denominador_final = denominador * denominador_2
        print("la cuenta quedaria tal que asi: " , numerador , "*" , numerador_2 , "sobre" , denominador_final )
            #ingresar = para imprimir el resultado final
        resultado_final = input("ingrese = para resultado final: ")
        if resultado_final == "=":
                #imprime resultado final
            print("el resultado seria: " ,numerador_final, "/", denominador_final)
        #division
    elif cuenta == "DIV":
            #numerador
        numerador_division = numerador * denominador_2
            #denominador
        denominador_division = numerador_2 * denominador
        print("la cuenta quedaria tal que asi: " , numerador , "*" , denominador_2 , "sobre" , denominador_division )
            #ingresar = para imprimir el resultado final
        resultado_final = input("ingrese = para resultado final: ")
        if resultado_final == "=":
                #imprime resultado final
            print("el resultado es: " ,numerador_division , "/" , denominador_division)
    else:
        print("error. Ingrese nuevamente")

#variable para iniciar
prender = str(input("ingrese 'on' para iniciar: "))
while prender != "on":
    prender = str(input("ingrese 'on' para iniciar: "))
#inicia la calculadora
while prender == "on":
    funcion = int(input("ingresar tipo de calculadora desea utilizar (1 clasica, 2 fracciones, 3 conversion, 4 para salir (off)): "))
    
    #selecciona calculadora clasica
    if funcion == 1:
        #llama a la funcion calculadora clasica
        fun_clasica()
        #ingresa tipo de cuenta
        cuenta = input("ingresar tipo de cuenta (SUM para suma, RES para resta, MUL para multiplicacion, DIV para division): ")
        #SUMA
        if cuenta == "SUM":
            #llama a la funcion de suma de calculadora clasica
            sum_clasica()
        #RESTA
        elif cuenta == "RES":
            #llama a la funcion de resta de calculadora clasica
            res_clasica()
        #MULTIPLICACION
        elif cuenta == "MUL":
            #llama a la funcion de multiplicacion de calculadora clasica
            mul_clasica()
        #DIVISION
        elif cuenta == "DIV":
            #llama a la funcion de division de calculadora clasica
            div_clasica()
    #selecciona calculadora de fracciones
    elif funcion == 2:
            cal_fracciones()


        
