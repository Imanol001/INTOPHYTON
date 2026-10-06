class Reales:
    """Implementacion del TAD Reales"""

    def suma(self, n1: float, n2: float) -> float:
        return n1 + n2

    def resta(self, n1: float, n2: float) -> float:
        return n1 - n2

    def multiplicacion(self, n1: float, n2: float) -> float:
        return n1 * n2

    def division(self, n1: float, n2: float) -> float:
        if n2 == 0:
            raise ValueError("No se puede dividir entre cero.")
        return n1 / n2


if __name__ == "__main__":
    print("Probando el TAD Reales")
    print("Valores: números reales")
    print("Operaciones: suma, resta, multiplicación, división")

    obj = Reales()
    opcion = -1

    while opcion != 0:
        print("\nOperaciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("0. Salir")

        try:
            opcion = int(input("Elige una operación: "))

            match opcion:
                case 1:
                    print("Ingresa 2 valores:")
                    n1 = float(input("Valor 1: "))
                    n2 = float(input("Valor 2: "))

                    resultado = obj.suma(n1, n2)
                    print(f"La suma de {n1} y {n2} es: {resultado}")

                case 2:
                    print("Ingresa 2 valores:")
                    n1 = float(input("Valor 1: "))
                    n2 = float(input("Valor 2: "))

                    resultado = obj.resta(n1, n2)
                    print(f"La resta de {n1} y {n2} es: {resultado}")

                case 3:
                    print("Ingresa 2 valores:")
                    n1 = float(input("Valor 1: "))
                    n2 = float(input("Valor 2: "))

                    resultado = obj.multiplicacion(n1, n2)
                    print(f"La multiplicación de {n1} y {n2} es: {resultado}")

                case 4:
                    print("Ingresa 2 valores:")
                    n1 = float(input("Valor 1: "))
                    n2 = float(input("Valor 2: "))

                    if n2 != 0:
                        resultado = obj.division(n1, n2)
                        print(f"La división de {n1} entre {n2} es: {resultado}")
                    else:
                        print("Error: no se puede dividir entre cero.")

                case 0:
                    print("Adios!!!")

                case _:
                    print("Opcion no valida")

        except ValueError:
            print("Error: Debes ingresar un número válido.")
