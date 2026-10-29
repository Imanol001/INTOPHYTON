tiempos = []

n = int(input("Cuantos tiempos de respuesta quiere ingresar? "))

for i in range(n):
    tiempo = int(input("Ingrese el tiempo de respuesta en ms: "))
    tiempos.append(tiempo)

print("\n---Reporte de latencia---")
print("Tiempos: ", tiempos)
print("Tiempo de respuesta mas alto: ", max(tiempos), "ms")
print("Tiempo de respuesta mas bajo: ", min(tiempos), "ms")
print("Tiempo de respuesta promedio: ", sum(tiempos) / len(tiempos), "ms")

mayor_frecuencia = 0
tiempo_repetido = []

for tiempo in tiempos:
    frecuencia = tiempos.count(tiempo)

    if frecuencia > mayor_frecuencia:
        mayor_frecuencia = frecuencia
        tiempo_repetido = tiempo

print("Tiempo de respuesta mas repetido: ", tiempo_repetido, "ms")
