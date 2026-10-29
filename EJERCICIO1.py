contraseña_correcta = "123"
intentos = 0

while intentos < 3:
    contraseña = input("Ingresa la contraseña: ")
    intentos += 1
    if contraseña == contraseña_correcta:
        print("Bienvenido, Acceso concedido.")
        break
    else:
        print(f"Contraseña incorrecta. Intento {intentos} de 3.")
    if intentos == 3 and contraseña != contraseña_correcta:
        print("Acceso bloqueado. Has superado los 3 intentos.")
