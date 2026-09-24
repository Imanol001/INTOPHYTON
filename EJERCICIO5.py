def validar_paswoord(pasword):
    pasword_correcto = "123"

    if pasword == pasword_correcto:
        return True
    else:
        return False


pasword = input("Ingrese la contraseña: ")
resultado = validar_paswoord(pasword)

if resultado:
    print("Contraseña correcta. Acceso concedido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")
