import random


class MatrizDinamica:
    def __init__(self, filas: int, columnas: int):
        self.filas = filas
        self.columnas = columnas
        self.matriz = []

    def llenar_matriz(self):
        for i in range(self.filas):
            fila_temporal = []
            for c in range(self.columnas):
                numero = random.randint(0, 5)
                fila_temporal.append(numero)
                self.matriz.append(fila_temporal)

    def mostrar_matriz(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                print(f"{self.matriz[f][c]}\t", end="")
            print()

    def contar_nodos(self):
        contador = 0
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.matriz[f][c] == 0:
                    contador = contador + 1
        return contador


def ejecutar():
    print("\n=====CONFIGURACION DEL PANEL=====")
    f = int(input("Escribe el numero de filas "))
    c = int(input("Escrie el numero de columnas "))

    mi_matriz = MatrizDinamica(f, c)
    mi_matriz.llenar_matriz()

    print("\n----ESTADO DEL PANEL DE NODOS----")
    mi_matriz.mostrar_matriz()

    nodos_fuera_linea = mi_matriz.contar_nodos()
    print("Total de nodos fuera de linea: ", nodos_fuera_linea)


if __name__ == "__main__":
    ejecutar()
