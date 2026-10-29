numeros = [1, 2, 3, 4, 5, 6]
multiplicador = int(input("Ingresa un valor "))

for i in range(len(numeros)):
    numeros[i] *= multiplicador

print("Numeros multiplicados por: ", multiplicador)
print(numeros)
