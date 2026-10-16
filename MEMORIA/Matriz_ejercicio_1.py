# PROMEDIO DE MATRIZ

filas = int(input("Ingresa el numero de filas: "))
columnas = int(input("Ingresa el numero de columnas: "))

matriz = []
suma = 0

for f in range(filas):
    fila = []
    for c in range(columnas):
        numero = int(input("Ingresa un numero: "))
        fila.append(numero)
        suma = suma + numero
    matriz.append(fila)

print("\n===MATRIZ===")
for fila in matriz:
    print(fila)

promedio = suma / (filas * columnas)
print("El promedio de la matriz es: ", promedio)
