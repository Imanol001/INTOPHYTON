saldo = 1000

while True:
    print("\n--- CAJERO AUTOMATICO ---")
    print("1. Consultar Saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("0. Salir")

    try:
        opcion = int(input("\nElige una opcion: "))

        match opcion:
            case 1:
                print(f"\nTu saldo actual es: ${saldo}")

            case 2:
                deposito = float(input("Ingresa la cantidad a depositar: "))

                if deposito <= 0:
                    print("Error: La cantidad a depositar debe ser mayor a cero.")
                else:
                    saldo += deposito
                    print(f"Deposito exitoso. Tu nuevo saldo es: ${saldo}")

            case 3:
                retiro = float(input("Ingresa la cantidad a retirar: "))

                if retiro <= 0:
                    print("Error: La cantidad a retirar debe ser mayor a cero.")
                elif retiro > saldo:
                    print("Error: Fondos insuficientes.")
                else:
                    saldo -= retiro
                    print(f"Retiro exitoso. Tu nuevo saldo es: ${saldo}")

            case 0:
                print("Saliendo del cajero automático...")
                break

            case _:
                print("Error. Opción no válida. Por favor, elige un número del 0 al 3.")

    except ValueError:
        print("Error: debes ingresar un número.")
