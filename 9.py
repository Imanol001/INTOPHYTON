try:
    # Codigo que podria fallar
    edad = int(input("Ingresa tu edad en numeros: "))
    print(f"Tienes {edad} años. ")
except ValueError:
    # Se ejecuta solo si el usuario teclea texto en lugar de numero
    print("Error, Debes ingresar un numero entero valido ")
