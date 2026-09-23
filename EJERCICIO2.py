materias = int(input("¿Cuantas materias cursaste? "))
suma = 0
for i in range(materias):
    calificacion = float(input(f"Ingresa la calificación de la materia {i + 1}: "))

    suma += calificacion

promedio = suma / materias

print(f"Tu promedio es: {promedio:.2f}")

if promedio >= 85:
    print("Eres apto para una beca.")
else:
    print("No eres apto para una beca.")
