#lista para funcion clasica
lista_funcion_clasica = []
#funcion calculadora clasica
def fun_clasica():
    #llamando a la lista que se definio antes
    global lista_funcion_clasica
        #ingreso numeros
    numeros_funcion_clasica = float(input("ingresar numero (o 0 para terminar): "))
    while numeros_funcion_clasica != 0:
            #se agregan los numeros a la lista
        lista_funcion_clasica.append(numeros_funcion_clasica)
        numeros_funcion_clasica = float(input("ingresar numero (o 0 para terminar): "))

#funcion suma de calculadora clasica
def sum_clasica():
    #llamando a la lista que se definio antes con los numeros ingresados previamente
    global lista_funcion_clasica
    #variable a la que se le van a sumar los num de la lista
    total_suma = 0
    #recorremos la lista
    for num in lista_funcion_clasica:
        #numeros de la lista sumado al cero de la variable
        total_suma += num
            #imprime resultado final
    resultado_final_sum = str(input("ingresar = para imprimir resultado: "))
    if resultado_final_sum == "=":
        print("total de suma es:", total_suma)
    else:
        print("error")
        #limpiar lista
    lista_funcion_clasica.clear()

#funcion resta de calculadora clasica
def res_clasica():
    #llamando a la lista que se definio antes con los numeros ingresados previamente
    global lista_funcion_clasica
    #verifica si la lista tiene numeros
    if len(lista_funcion_clasica) > 0:
        #se asigna el primer elemento de la lista a la variable
        total_resta = lista_funcion_clasica[0]
    #se recorre el segundo numero de la lista
    for num in lista_funcion_clasica[1:]:
        #se hace la cuenta
        total_resta -= num
                #imprime resultado final
    resultado_final_resta = str(input("ingresar = para imprimir resultado: "))
    if resultado_final_resta == "=":
        print("total de resta es:", total_resta)
    else:
        print("lista vacia")
        #limpiar lista
    lista_funcion_clasica.clear()

#funcion multiplicacion de calculadora clasica
def mul_clasica():
    #llamando a la lista que se definio antes con los numeros ingresados previamente
    global lista_funcion_clasica
    #verifica si la lista tiene numeros
    if len(lista_funcion_clasica) > 0:
        #variable por la cual se van a multiplicar los numeros de la lista
        total_multiplicacion = 1
        
        for num in lista_funcion_clasica:
            total_multiplicacion *= num
                #imprime resultado final
        resultado_final_multiplicacion = str(input("ingresar = para imprimir resultado: "))
        if resultado_final_multiplicacion == "=":
            print("total de multiplicacion es:", total_multiplicacion)
        else:
            print("lista vacia")
            #limpiar lista
    lista_funcion_clasica.clear()

#funcion division de calculadora clasica
def div_clasica():
    #llamando a la lista que se definio antes con los numeros ingresados previamente
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
            #limpiar lista
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
            print("ingrese un denominador distinto de 0")
        #tipo de cuenta que se ingresa
    cuenta = input("ingresar tipo de cuenta (SUM para suma, RES para resta, MUL para multiplicacion, DIV para division): ")
        #suma
    if cuenta == "SUM":
            #se busca denominador comun
        den_comun = denominador * denominador_2
        print("el denominador comun seria:", den_comun)
            #se busca el primer numerador
        num_comun_1 = numerador * denominador_2
        print("el primer numerador es:", num_comun_1)
            #se busca el segundo numerador
        num_comun_2 = numerador_2 * denominador
        print("el segundo numerador es:", num_comun_2)
            #se suman los dos numeradores
        suma_num = num_comun_1 + num_comun_2
        print("la cuenta quedaria tal que asi: " , num_comun_1, "+" , num_comun_2 , "sobre" , den_comun)
            #ingresar = para imprimir el resultado final
        resultado_final = input("ingrese = para resultado final: ")
        if resultado_final == "=":
                #imprime resultado final
                print("el resultado es: ",suma_num,"/",den_comun)
        #resta
    elif cuenta == "RES":
            #se busca denominador comun
        den_comun = denominador * denominador_2
        print("el denominador comun seria:", den_comun)
            #se busca el primer numerador
        num_comun_1 = numerador * denominador_2
        print("el primer numerador es:", num_comun_1)
            #se busca el segundo numerador
        num_comun_2 = numerador_2 * denominador
        print("el segundo numerador es:", num_comun_2)
            #la resta de los numeradores
        resta_num = num_comun_1 - num_comun_2
        print("la cuenta quedaria tal que asi: ", num_comun_1 , "-" , num_comun_2 , "sobre" , den_comun )
            #ingresar = para imprimir el resultado final
        resultado_final = input("ingrese = para resultado final: ")
        if resultado_final == "=":
                #imprime resultado final
            print("el resultado es:",resta_num,"/",den_comun)
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


#<----------------------------------><------------------------------------------>

#funcion para calculadora de conversion
#funcion binaria
def conv_bi():
    numero = int(input("Ingrese numero decimal: "))
    # error si el numero ingresado es menor a 0
    if numero < 0:
        print("error. numero invalido")
    # error si el numero ingresado es mayor a 4 digitos
    elif numero > 9999:
        print("error. numero invalido")
    else:
        digitos_binarios = []  # lista para los digitos binarios
        while numero > 0:
            digitos_binarios.append(str(numero % 2))
            numero = numero // 2
        # aca se unen los binarios y se imprime al reves
        resultado = ''.join(reversed(digitos_binarios))
        resultado_bi = input("ingrese = para finalizar: ")
        if resultado_bi == "=":
            print(f"numero en binario es: {resultado}")


#funcion hexadecimal
def conv_hex():
    numero = int(input("ingrese numero decimal: "))
#error si el numero ingresado es mayor a 4 digitos
    while numero > 9999 or numero < 0:
        print("numero ingresado no valido")
    numero = int(numero)
    hexadecimales = []  # lista donde se almacenan los residuos 
    # variables para guardar los residuos mayores a 9 y pasarlo a letra
    letras = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while numero > 0:
        residuo = numero % 16
        if residuo < 10:
            hexadecimales.append(str(residuo))
        else:
            digito = letras[residuo]
            hexadecimales.append(digito)
        numero = numero // 16
    #aca se unen los numeros hexadecimales y se imprimen al reves
    resultado = ''.join(reversed(hexadecimales))
    resultado_hex = input("ingrese = para finalizar: ")
    if resultado_hex == "=":
        print(f"el numero en hexadecimal es: {resultado}")
#funcion octal
def conv_oct():
    numero = int(input("ingrese numero decimal: "))
    numero_octal = ""
# error si el numero ingresado es mayor a 4 digitos
    while numero > 9999 or numero < 0:
        numero = int(input("numero ingresado no valido"))
    while numero > 0:
        residuo = numero % 8    
        numero_octal = str(residuo) + numero_octal
        numero = numero // 8
    resultado_oct = input("ingrese = para finalizar: ")
    if resultado_oct == "=":
        print("el numero en octal es: ", numero_octal)




#<------------------INICIA CALCULADORA------------------------------->                    

#variable para iniciar
prender = str(input("ingrese 'on' para iniciar: "))
while prender != "on":
    prender = str(input("ingrese 'on' para iniciar: "))
#inicia la calculadora
while prender == "on":
    funcion = int(input("ingresar tipo de calculadora desea utilizar:\n1 clasica\n2 fracciones\n3 conversion\n4 para salir (off): "))
    
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
    elif funcion == 3:
        conversion = str(input("ingrese el tipo de conversion que desea (BI para binario, HEX para hexadecimal, OCT para octal): "))
        if conversion == "BI":
            conv_bi()
        elif conversion == "HEX":
            conv_hex()
        elif conversion == "OCT":
            conv_oct()
    elif funcion == 4:
        print("apagado")
        break
    else:
        print("ingreso invalido")




print("""
.............      ........           ........         .........          .           ........            .........
.                  .      .          .        .        .                  .          .        .           .
.                  .      .         .          .       .                  .         .          .          .........
.    ...           ........        ..............      .                  .        ..............                 .
.      .           .      .       .              .     .                  .       .              .                .
........           .       .     .                .    .........          .      .                .       .........
""")






        
