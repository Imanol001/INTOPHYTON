# Registro de Calificaciones
calificaciones = []

for i in range(5):
    calificacion = float(input("ingresa una calificacion: "))
    calificaciones.append(calificacion)

print("\n ***REPORTE DE CALIFICACIONES*** ")
print("Califiacion mas alta: ", max(calificaciones))
print("Calificacion mas baja: ", min(calificaciones))
promedio = sum(calificaciones) / len(calificaciones)
print("Promedio de calificaciones: ", promedio)

if promedio >= 70:
    print("Resultado: Aprobado ")

else:
    print("Resultado: Reprobado ")
