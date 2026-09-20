def calculadora_basica():
    opcion = -1
    while opcion != 0:
        print("\n--- CALCULADORA BASICA ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Salir")
        try:
            opcion = int(input("\n Elige una Operacion: "))
            match opcion:
                case 1:
                    print("\n -- SUMA--")
                    a = float(input("Ingresa el primer numero: "))
                    b = float(input("Ingresa el segundo numero: "))
                    print(f"Resultado: {a} + {b} = {a + b}")
                case 2:
                    print("\n --RESTA-- ")
                    a = float(input("Ingresa el primer numero: "))
                    b = float(input("Ingresa el segundo numero: "))
                    print(f"Resultado: {a} - {b} = {a - b}")
                case 3:
                    a = float(input("Ingresa el primer numero: "))
                    b = float(input("Ingresa el segundo numero: "))
                    print(f"Resultado: {a} * {b} = {a * b}")
                case 4:
                    a = float(input("Igresa el primer numero: "))
                    b = float(input("Ingresa el segundo numero: "))
                    if b == 0:
                        print("Error matematico, no se puede dividir entre cero")
                    else:
                        print(f"Resultado: {a} / {b} = {a / b}")
                case 0:
                    print("Saliendo de la calculadora... ")
                case _:
                    print(
                        "Error. Ocion no valida. Por favor, elige un numero del 0 al 4. "
                    )

        except ValueError:
            # Este except atrapara el error si el escriben letras en el menu o letras en los numeros.
            print("Error de formato: Debes ingresar un valor numerico valido")


calculadora_basica()
