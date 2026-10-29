calificacion = int(input("Introduce tu calificación: "))

if calificacion == 100:
    print("¡Calificaión perfecta!")
elif calificacion >= 70:
    # Se ejecuta la condicion del 'if' fue falsa, pero esta es verdadera
    print("Aprobado")
else:
    # Se ejecuta si ninguna de las condiciones anteriores fue verdadera
    print("Reprobado")
