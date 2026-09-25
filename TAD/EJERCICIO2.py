class Numeros:
    """Implementacion del TAD Numeros"""

    def suma(self, numero1: complex, numero2: complex) -> complex:
        return numero1 + numero2

    def resta(self, numero1: complex, numero2: complex) -> complex:
        return numero1 - numero2

    def producto(self, numero1: complex, numero2: complex) -> complex:
        return numero1 * numero2

    def division(self, numero1: complex, numero2: complex) -> complex:
        return numero1 / numero2


if __name__ == "__main__":
    print("Probando el TAD Numeros")
    print("Valores reales o complejos")
    print("Ejemplos: 5, 3.5, 2+3j")

    obj = Numeros()
    opcion = -1

    while opcion != 0:
        print("\nOperaciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Producto")
        print("4. División")
        print("0. Salir")

        try:
            opcion = int(input("\nElige una opción: "))

            match opcion:
                case 1:
                    n1 = complex(input("Valor 1: "))
                    n2 = complex(input("Valor 2: "))
                    resultado = obj.suma(n1, n2)
                    print(f"El resultado de la suma es: {resultado}")

                case 2:
                    n1 = complex(input("Valor 1: "))
                    n2 = complex(input("Valor 2: "))
                    resultado = obj.resta(n1, n2)
                    print(f"El resultado de la resta es: {resultado}")

                case 3:
                    n1 = complex(input("Valor 1: "))
                    n2 = complex(input("Valor 2: "))
                    resultado = obj.producto(n1, n2)
                    print(f"El resultado del producto es: {resultado}")

                case 4:
                    n1 = complex(input("Valor 1: "))
                    n2 = complex(input("Valor 2: "))

                    if n2 == 0:
                        print("Error: no se puede dividir entre cero.")
                    else:
                        resultado = obj.division(n1, n2)
                        print(f"El resultado de la división es: {resultado}")

                case 0:
                    print("Adios!!!")

                case _:
                    print("Opción no válida")

        except ValueError:
            print("Error: debes ingresar un número válido.")
