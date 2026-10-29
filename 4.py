boletos_disponibles = int(input("Cuantos boletos tiene para vender?: "))

while boletos_disponibles > 0:
    print(f"Vendiendo boleto. Quedan {boletos_disponibles}")
    boletos_disponibles -= 1  # Equivalente a: boletos = boletos - 1

print("Boletos agotados. ")
