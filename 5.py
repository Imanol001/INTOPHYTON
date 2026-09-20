# range(5) genera los numeros: 0, 1, 2, 3, 4 (siempre se detiene uno antes)
for i in range(5):
    print(f"Iteracion número {i}")

# range(inicio, fin) -> Comienza en 1, termina en 3 (uno antes del 4)
for i in range(1, 4):
    print(f"Contando: {i}")

estudiantes = ["Ana", "Carlos", "Beatriz"]

# En lugar de hacer un for con un contador 'i' y usar estudiantes [i]:
for estudiante in estudiantes:
    print(f"Revisando tarea de {estudiante}")
