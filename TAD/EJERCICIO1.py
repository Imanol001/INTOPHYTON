class NaturalCompara:
    """Implementacion del TAD NaturalCompara"""

    def mayor(self, numero1: int, numero2: int) -> int:
        if numero1 > numero2:
            return numero1
        else:
            return numero2

    def menor(self, numero1: int, numero2: int) -> int:
        if numero1 < numero2:
            return numero1
        else:
            return numero2

    def igual(self, numero1: int, numero2: int) -> bool:
        return numero1 == numero2

    def diferente(self, numero1: int, numero2: int) -> bool:
        return numero1 != numero2


if __name__ == "__main__":
    print("Probando el TAD NaturalCompara")
    print("Valores: 0, 1, 2...")

    obj = NaturalCompara()
    opcion = -1

    while opcion != 0:
        print("\nOperaciones:")
        print("1. Mayor")
        print("2. Menor")
        print("3. Igual")
        print("4. Diferente")
        print("0. Salir")

        try:
            opcion = int(input("\nElige una opción: "))

            match opcion:
                case 1:
                    n1 = int(input("Valor 1: "))
                    n2 = int(input("Valor 2: "))
                    resultado = obj.mayor(n1, n2)
                    print(f"El número mayor es: {resultado}")

                case 2:
                    n1 = int(input("Valor 1: "))
                    n2 = int(input("Valor 2: "))
                    resultado = obj.menor(n1, n2)
                    print(f"El número menor es: {resultado}")

                case 3:
                    n1 = int(input("Valor 1: "))
                    n2 = int(input("Valor 2: "))
                    resultado = obj.igual(n1, n2)
                    print(f"Los números son iguales?: {resultado}")

                case 4:
                    n1 = int(input("Valor 1: "))
                    n2 = int(input("Valor 2: "))
                    resultado = obj.diferente(n1, n2)
                    print(f"Los números son diferentes?: {resultado}")

                case 0:
                    print("Adios!!!")

                case _:
                    print("Opción no válida")

        except ValueError:
            print("Error: debes ingresar un número entero válido.")
