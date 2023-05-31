prender = str(input("Ingrese 'on' para iniciar: "))
while prender == "on":
    numeros = 0
    funcion = int(input("ingrese que tipo de calculadora (1 clasica, 2 fracciones, 3 conversion, 4 para salir(off)): "))
    if funcion == 1:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        operacion = input("Ingrese qué operación desea realizar (suma, resta, multiplicacion, division): ")
        if operacion == "suma":
            resultado_final_clasica = input("ingrese = para imprimir resultado: ")
            resultado_suma = num1 + num2
            print(f"su resultado es: " , resultado_suma)
        elif operacion == "resta":
            resultado_final_clasica = input("ingrese = para imprimir resultado: ")
            resultado_resta = num1 - num2
            print(f"su resultado es: " , resultado_resta)
        elif operacion == "multiplicacion":
            resultado_final_clasica = input("ingrese = para imprimir resultado: ")
            resultado_multiplicacion = num1 * num2
            print(f"su resultado es: " , resultado_multiplicacion)
        elif operacion == "division":
            if num2 == 0:
                print("Error, el segundo número no puede ser 0")
            else:
                resultado_final_clasica = input("ingrese = para imprimir resultado: ")
                resultado_division = num1 // num2
                print(f"su resultado es: " , resultado_division)

        # numero_extra = str(input("desea seguir agregando numeros SI o = para imprimir resultado: "))
        # if numero_extra == "SI":
        #     numeros += 1
        #     numero = float(input("ingrese el numero {} de su operacion: " .format(numeros)))
        #     operacion = input("Ingrese qué operación desea realizar (suma, resta, multiplicacion, division) o ingrese 0 para terminar: ")
        #     if operacion == "suma":
        #         print("Su resultado es:", num1 + num2 + numero)
        #     elif operacion == "resta":
        #         print("Su resultado es:", num1 - num2 - numero)
        #     elif operacion == "multiplicacion":
        #         print("Su resultado es:", num1 * num2 * numero)
        #     elif operacion == "division":
        #         if num2 == 0:
        #             print("Error, el segundo número no puede ser 0")
        #     else:
        #         print("Su resultado es:", num1 / num2 / numero)
        # if numero_extra == "=":
        #     print("finalizo")
    #funcion 3 conversion
    elif funcion == 3:
        conversion = str(input("ingrese el tipo de conversion que desea (BI para binario, HEX para hexadecimal, OCT para octal): "))
        if conversion == "BI":
                numero = int(input("Ingrese un número decimal: "))
                # error si el número ingresado es menor a 0
                if numero < 0:
                    print("Error: número inválido.")
                # error si el número ingresado es mayor a 4 dígitos
                elif numero > 9999:
                    print("Número ingresado no válido.")
                else:
                    digitos_binarios = []  # Lista para los dígitos binarios
                    while numero > 0:
                        digitos_binarios.append(str(numero % 2))
                        numero = numero // 2
                    # aca se unen los binarios y se imprime al reves
                    resultado = ''.join(reversed(digitos_binarios))
                    resultado_bi = input("Ingrese = para finalizar: ")
                    if resultado_bi == "=":
                        print(f"El número en binario es: {resultado}")
    #--------------------------><----------------------------------------
        elif conversion == "HEX":
            numero = int(input("Ingrese número: "))
    #error si el numero ingresado es mayor a 4 digitos
            while numero > 9999 or numero < 0:
                print("numero ingresado no valido.")
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
                print(f"El número en hexadecimal es: {resultado}")
            break

    #---------------------------><---------------------------------------
        elif conversion == "OCT":
            numero = int(input("Ingrese un número decimal: "))
            numero_octal = ""
            # Corrección: Verificar si el número ingresado tiene más de 4 dígitos o es menor a 0
            while numero > 9999 or numero < 0:
                numero = int(input("El número ingresado no es válido. Ingrese otro número decimal: "))
            while numero > 0:
                residuo = numero % 8    
                numero_octal = str(residuo) + numero_octal
                numero = numero // 8
            resultado_oct = input("Ingrese = para finalizar: ")
            if resultado_oct == "=":
                print("El número en octal es:", numero_octal)
    elif funcion == 4:
        print("apagado")
        break
    else:
        print("ingreso invalido")