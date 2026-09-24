def calcular_promedio(calif1, calif2, calif3):
    promedio = (calif1 + calif2 + calif3) / 3
    return promedio


calif1 = float(input("Ingresa la primera calificacion: "))
calif2 = float(input("Ingresa la segunda calificacion: "))
calif3 = float(input("Ingresa la tercera calificacion: "))

promedio = calcular_promedio(calif1, calif2, calif3)
print(f"Tu promedio es de: {promedio}")
