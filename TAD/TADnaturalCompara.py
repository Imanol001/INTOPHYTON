class NaturalCompara:

    def menorIgual(self, n1: int, n2: int) -> bool:
        return n1 <= n2

    def menor(self, n1: int, n2: int) -> bool:
        return n1 < n2

    def mayor(self, n1: int, n2: int) -> bool:
        return n1 > n2

    def mayorIgual(self, n1: int, n2: int) -> bool:
        return n1 >= n2


if __name__ == "__main__":
    print("Probando el TAD NaturalCompara")
    print("Valores: 1,2.....")
    print("Operaciones: menorIgual, menor, mayor, mayorIgual")

    obj = NaturalCompara()
    opcion = -1

    while opcion != 0:
        print("\nOperaciones:")
        print("1. MenorIgual")
        print("2. Menor")
        print("3. Mayor")
        print("4. MayorIgual")
        print("0. Salir")

        try:
            opcion = int(input("Elige una operación: "))

            match (opcion):
                case 1:
                    print("Ingresa 2 valores: ")
                    n1 = int(input("Valor 1: "))
                    n2 = int(input("Valor 2: "))

                    resultado = obj.menorIgual(n1, n2)
                    print(f"{n1} es menor o igual que {n2}?: {resultado}")

                case 2:
                    print("Ingresa 2 valores: ")
                    n1 = int(input("Valor 1: "))
                    n2 = int(input("Valor 2: "))

                    resultado = obj.menor(n1, n2)
                    print(f"{n1} es menor que {n2}?: {resultado}")

                case 3:
                    print("Ingresa 2 valores: ")
                    n1 = int(input("Valor 1: "))
                    n2 = int(input("Valor 2: "))

                    resultado = obj.mayor(n1, n2)
                    print(f"{n1} es mayor que {n2}?: {resultado}")

                case 4:
                    print("Ingresa 2 valores: ")
                    n1 = int(input("Valor 1: "))
                    n2 = int(input("Valor 2: "))

                    resultado = obj.mayorIgual(n1, n2)
                    print(f"{n1} es mayor o igual que {n2}?: {resultado}")

                case 0:
                    print("Adios!!!")

                case _:
                    print("Opcion no valida")
        except ValueError:
            print("Error: Debes ingresar un número entero.")
