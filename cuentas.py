prender = str(input("Ingrese 'on' para iniciar: "))
while prender == "on":
    funcion = int(input("ingresar tipo de calculadora desea utilizar (1 clásica, 2 fracciones, 3 conversión, 4 para salir (off)): "))
    if funcion == 1:
        lista_funcion_clasica = []
        numeros_funcion_clasica = float(input("Ingresar numero (o 0 para terminar): "))
        while numeros_funcion_clasica != 0:
            lista_funcion_clasica.append(numeros_funcion_clasica)
            numeros_funcion_clasica = float(input("Ingresar numero (o 0 para terminar): "))
        cuenta = input("ingresar tipo de cuenta (SUM para suma, RES para resta, MUL para multiplicacion, DIV para division): ")
        if cuenta == "SUM":
            total_suma = 0
            for num in lista_funcion_clasica:
                total_suma += num
            
            resultado_final_sum = str(input("ingresar = para imprimir resultado: "))
            if resultado_final_sum == "=":
                print("total de suma es:", total_suma)

        if cuenta == "RES":
            if len(lista_funcion_clasica) > 0:
                total_resta = lista_funcion_clasica[0]
                for num in lista_funcion_clasica[1:]:
                    total_resta -= num

                resultado_final_resta = str(input("ingresar = para imprimir resultado: "))
                if resultado_final_resta == "=":
                    print("total de resta es:", total_resta)
            else:
                print("lista vacia")
        elif cuenta == "MUL":
            if len(lista_funcion_clasica) > 0:
                total_multiplicacion = 1
                for num in lista_funcion_clasica:
                    total_multiplicacion *= num

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
                print("lista vacia")






        

    # funcion 3 conversion
    elif funcion == 3:
        conversion = str(input("ingrese el tipo de conversion que desea (BI para binario, HEX para hexadecimal, OCT para octal): "))
        if conversion == "BI":
            numero = input("ingrese numero: ")
            #error si el numero ingresado es mayor a 4 digitos
            if len(numero) > 4:
                print("numero ingresado no es válido.")
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
                print("numero ingresado no valido.")
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
                print("numero ingresado no es válido.")
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