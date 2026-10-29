materias = int(input("¿Cuantas materias cursas? "))

while materias <= 0:
    print("Debes ingresar al menos una materia.")
    materias = int(input("¿Cuantas materias cursas? "))

aprobadas = 0

for i in range(materias):
    calificacion = float(input(f"Ingresa la calificacion de la materia {i + 1}: "))

    if calificacion >= 70:
        print(f"La materia {i + 1} está aprobada.")
        aprobadas += 1
    else:
        print(f"La materia {i + 1} no está aprobada.")

if aprobadas == materias:
    print("Felicidades, aprobaste todas las materias.")
else:
    print(f"Aprobaste {aprobadas} de {materias} materias.")
