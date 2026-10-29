# Funcion con parametros y sin retorno
def areaTriangulo(b: float, a: float):
    area = b * a / 2
    print(f"El area del triangulo es: {area}")


areaTriangulo(5, 4)


# Funcion sin parametros y sin retorno
def areaT():
    b = float(input("Introduce la base: "))
    a = float(input("Introduce la altura: "))
    print(f"El area del triangulo es: {b*a/2}")
