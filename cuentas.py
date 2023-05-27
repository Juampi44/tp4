#variable para iniciar
prender = str(input("Ingrese 'on' para iniciar: "))
#inicia la calculadora
while prender == "on":
    funcion = int(input("ingresar tipo de calculadora desea utilizar (1 clásica, 2 fracciones, 3 conversión, 4 para salir (off)): "))
    #funcion calculadora clasica
    if funcion == 1:
        #lista donde se guardan los numeros ingresados
        lista_funcion_clasica = []
        #ingreso numeros
        numeros_funcion_clasica = float(input("Ingresar numero (o 0 para terminar): "))
        while numeros_funcion_clasica != 0:
            #se agregan los numeros a la lista
            lista_funcion_clasica.append(numeros_funcion_clasica)
            numeros_funcion_clasica = float(input("Ingresar numero (o 0 para terminar): "))
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
        #resta
        if cuenta == "RES":
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
                print("lista vacia")

#---------------------------------------------------->>----------------------------------------------------                
                
    elif funcion == 2:
        print("fracciones")
        def encontrar_mcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def simplificar(num, den):
            if den == 0:
                raise ValueError("El denominador no puede ser cero.")
            mcd = encontrar_mcd(num, den)
            return num // mcd, den // mcd

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

            while opcion != "salir":
                if opcion == "suma" or opcion == "resta" or opcion == "multiplicacion" or opcion == "division":
                    try:
                        fraccion = ingresarFraccion()
                        fracciones.append(fraccion)
                    except ValueError as error:
                        print(str(error))
                elif opcion == "salir":
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")
                if opcion == "suma":
                    resultado = sumar(fracciones)
                    print(f"Resultado de la suma y/o la simplificación es: {resultado[0]}/{resultado[1]}")
                elif opcion == "resta":
                    resultado = restar(fracciones)
                    print(f"Resultado de la resta y/o la simplificación es: {resultado[0]}/{resultado[1]}")
                elif opcion == "multiplicacion":
                    resultado = multiplicar(fracciones)
                    print(f"Resultado de la multiplicación y/o la simplificación es: {resultado[0]}/{resultado[1]}")
                elif opcion == "division":
                    resultado = dividir(fracciones)
                    print(f"Resultado de la división y/o la simplificación es: {resultado[0]}/{resultado[1]}")

                opcion = input("Ingrese una operación (suma, resta, multiplicacion, division) o 'salir' para terminar: ")

        opcion = input("Ingrese una operación (suma, resta, multiplicacion, division) o 'salir' para terminar: ")
        opciones(opcion)





        

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