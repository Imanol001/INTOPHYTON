class Recursividad:

    # 1.Factorial

    def factorial_iterativo(self, n: int) -> int:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    def factorial_recursivo(self, n: int) -> int:
        if n == 0:  # Caso Base
            return 1
        else:  # Caso Recursivo
            return n * self.factorial_recursivo(n - 1)

    # 2.Fibonacci

    def fibonacci_iterativo(self, n: int) -> int:
        if n <= 1:
            return n
        f1, f2 = 1, 1
        while n > 2:
            nuevo = f1 + f2
            f1 = f2
            f2 = nuevo
            n -= 1
        return f2

    def fibonacci_recursivo(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.fibonacci_recursivo(n - 1) + self.fibonacci_recursivo(n - 2)

    # 3.Problema 1: Trampa - Error de Memoria

    def repetir(self):
        # Esto generará un RecursionError en Python, equivalente
        # al StackOverfLowException
        self.repetir()

    # 4. Problemas 2: Impresion descendente sin caso base

    def imprimir_sin_base(self, x: int):
        print(x, end=" ")
        self.imprimir_sin_base(x - 1)

    # 5.Problema 3: Impresion descendente

    def imprimir_descendente(self, x: int):
        # Se agrega la validación x > 0 para evitar el ciclo infinito
        # y que se detenga en 1[cite: 3].
        if x > 0:
            print(x, end=" ")
            self.imprimir_descendente(x - 1)

    # 6.Problema: Impresion Ascendente de 1 a 5

    def imprimir_ascendente(self, x: int):
        # La magia ocurre al intercambiar el orden: primero la llamada
        # recursiva y luego la impresion. Así se imprime al "desarrollar" el stack
        if x > 0:
            self.imprimir_ascendente(x - 1)
            print(x, end=" ")

    # 7.Priblema 4: Inversor de Cadenas

    def invertir_cadena(self, cadena: str) -> str:
        if len(cadena) < 1:
            return cadena
        else:
            return self.invertir_cadena(cadena[1:]) + cadena[0]

    # 8.Ejercicio Ecuacion Recurrente

    # a_n = a_{n - 1} + 2^n, a_0 = 1
    def ecuacion_recurrente(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            return self.ecuacion_recurrente(n - 1) + (2**n)

    # 9.Ejercicio Personal: Suma Recursiva
    def suma_recursiva(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            return n + self.suma_recursiva(n - 1)


# MENU DE PRUEBAS
if __name__ == "__main__":
    re = Recursividad()
    opcion = -1

    while opcion != 0:
        print("\n\n-----MENU RECURSIVIDAD-----")
        print("1. Factorial (Iterativo vs Recursivo)")
        print("2. Fibonacci (Iterativo vs Recursivo)")
        print("3. Problema 1: Desbordamiento de Pila (Crash Intencional)")
        print("4. Problema 2: Impresion descendente sin caso base")
        print("5. Problema 3: Imprimir descendente (5 a 1)")
        print("6. Problem extra: Imprimir Ascendente (1 a 5)")
        print("7. Problema 4: Invertir cadena")
        print("8. Ecuacion Recurrente")
        print("9. Ejercicio Personal: Suma Recursiva")
        print("0. salir")

        try:
            opcion = int(input("Elige una opcion: "))

            match opcion:
                case 1:
                    num = int(input("Ingresa un numero para calcular factorial: "))
                    print(f"Iterativo: {re.factorial_iterativo(num)}")
                    print(f"Recursivo: {re.factorial_recursivo(num)}")

                case 2:
                    num = int(input("Ingresa la posicion de Fibonacci: "))
                    print(f"Iterativo: {re.fibonacci_iterativo(num)}")
                    print(f"Recursivo: {re.fibonacci_recursivo(num)}")

                case 3:
                    print("Iniciando recursion infinita... ¡Preparate para el error!")
                    re.repetir()

                case 4:
                    num = int(input("Ingresa el número inicial: "))
                    re.imprimir_sin_base(num)

                case 5:
                    num = int(input("Ingresa el numero inicial (ej. 5): "))
                    re.imprimir_descendente(num)

                case 6:
                    num = int(input("Ingresa el  limite superior (ej. 5): "))
                    re.imprimir_ascendente(num)

                case 7:
                    texto = input("Introduce una palabra: ")
                    print(f"Palabra invertida: {re.invertir_cadena(texto)}")

                case 8:
                    num = int(input("Ingresa el valor de 'n' para la ecuacion: "))
                    print(f"Resultado: {re.ecuacion_recurrente(num)}")

                case 9:
                    num = int(input("Ingresa un numero entero no negativo: "))
                    print(f"Suma recursiva: {re.suma_recursiva(num)}")

                case 0:
                    print("saliendo del menu...")

                case _:
                    print("Opcion no valida")

        except ValueError:
            print("Entrada invalida. Asegurate de ingresar un numero entero.")
        except RecursionError as e:
            print("\n[ERROR ATRAPADO] se detuvo el proceso por desbordamiento de pila:")
            print(f"Mensaje del sistema: {e}")
