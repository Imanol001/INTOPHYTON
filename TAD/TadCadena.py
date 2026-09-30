class cadena:
    """Implementacion del TAD Cadena (String)"""

    def Concatenar(self, cadena1: str, cadena2: str) -> str:
        return cadena1 + cadena2

    def Longitud(self, cadena: str) -> int:
        return len(cadena)

    def es_vacia(self, cadena: str) -> bool:
        return cadena == ""

    def son_iguales(self, cadena1: str, cadena2: str) -> bool:
        return cadena1 == cadena2


if __name__ == "__main__":
    print("Probando el TAD Cadena")
    print('Valores: "Hola" y "Mundo"')
    print("Operaciones: Concatenar, Longitud, es_vacia, son_iguales")

    obj = cadena()

    cadena1 = "Hola"
    cadena2 = "Mundo"

    opcion = -1
while opcion != 0:
    print("\nOperaciones:")
    print("1. Concatenar")
    print("2. Longitud")
    print("3. Comprobar si es vacía")
    print("4. Comparar cadenas")
    print("0. Salir")

    try:
        opcion = int(input("Elige una opción: "))

        match (opcion):
            case 1:
                resultado = obj.Concatenar(cadena1, cadena2)
                print(f"La concatenacion de: {cadena1} y {cadena2} es: {resultado}")

            case 2:
                resultado1 = obj.Longitud(cadena1)
                resultado2 = obj.Longitud(cadena2)
                print(f"La longitud de '{cadena1}' es: {resultado1}")
                print(f"La longitud de '{cadena2}' es: {resultado2}")

            case 3:
                resultado1 = obj.es_vacia(cadena1)
                resultado2 = obj.es_vacia(cadena2)
                print(f"¿'{cadena1}' está vacía?: {resultado1}")
                print(f"¿'{cadena2}' está vacía?: {resultado2}")

            case 4:
                resultado = obj.son_iguales(cadena1, cadena2)
                print(f"¿'{cadena1}' y '{cadena2}' son iguales?: {resultado}")

            case 0:
                print("Adios!!!")

            case _:
                print("Opción no válida")

    except ValueError:
        print("Error: debes ingresar un número entero válido.")
