#variable para iniciar
prender = str(input("ingrese 'on' para iniciar: "))
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
            total_suma = 0
            for num in lista_funcion_clasica:
                total_suma += num
            #imprime resultado final
            resultado_final_sum = str(input("ingresar = para imprimir resultado: "))
            if resultado_final_sum == "=":
                print("total de suma es:", total_suma)
            else:
                print("error")
        #resta
        elif cuenta == "RES":
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

#---------------------------------------------------->>----------------------------------------------------                
                #se ingresa 2
    elif funcion == 2:
        #ingresa primer numerador
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
            #ingresar = para imprimir el resultado final
            resultado_final = input("ingrese = para resultado final: ")
            if resultado_final == "=":
                #imprime resultado final
                print("el resultado es: " ,numerador_division , "/" , denominador_division)

#----------------------------------------->---------------------------------

    # funcion 3 conversion
    elif funcion == 3:
        conversion = str(input("ingrese el tipo de conversion que desea (BI para binario, HEX para hexadecimal, OCT para octal): "))
        if conversion == "BI":
            numero = input("ingrese numero: ")
            #error si el numero ingresado es mayor a 4 digitos
            if len(numero) > 4:
                print("numero ingresado no es valido.")
            else:
                numero = int(numero)
                digitos_binarios = []  # Lista para los dígitos binarios

                while numero > 0:
                    digitos_binarios.append(str(numero % 2))
                    numero = numero // 2

                # aca se unen los binarios y se imprime al reves
                resultado = ''.join(reversed(digitos_binarios))

                resultado_bi = input("ingrese = para finalizar: ")
                if resultado_bi == "=":
                    print(f"numero en binario es: {resultado}")
                
    #--------------------------><----------------------------------------
        elif conversion == "HEX":
            numero = input("Ingrese nnmero: ")

    #error si el numero ingresado es mayor a 4 digitos
            if len(numero) > 4:
                print("numero ingresado no valido")
            else:
                numero = int(numero)
                hexadecimales = []  # lista donde se almacenan los residuos 

                # variables para guardar los residuos mayores a 9 y pasarlo a letra
                letras = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

                while numero > 0:
                    residuo = numero % 16
                    if residuo < 10:
                        hexadecimales.append(str(residuo))
                    else:
                        dígito = letras[residuo]
                        hexadecimales.append(dígito)
                    numero = numero // 16

                #aca se unen los numeros hexadecimales y se imprimen al reves
                resultado = ''.join(reversed(hexadecimales))
                resultado_hex = input("ingrese = para finalizar: ")
                if resultado_hex == "=":
                    print(f"numero en hexadecimal es: {resultado}")
                
    #---------------------------><---------------------------------------
        elif conversion == "OCT":
            numero = input("ingrese numero decimal: ")
            numero_octal = ""
            #error si el numero ingresado es mayor a 4 digitos
            if len(numero) > 4:
                print("numero ingresado no es valido")
            else:
                numero = int(numero)
                while numero > 0:
                    residuo = numero % 8
                    numero_octal = str(residuo) + numero_octal
                    numero = numero // 8
            
            resultado_oct = input("ingrese = para finalizar: ")
            if resultado_oct == "=":
                print(f"nmero en octal es:", numero_octal)
            
    
    elif funcion == 4:
        print("apagado")
        break
    else:
        print("ingreso invalido")