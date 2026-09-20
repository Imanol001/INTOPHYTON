def ejecutar_comando(comando):
    match comando:
        case "iniciar":
            print("El sistema esta arrancando...")

        case "pausar":
            print("Sistema en pausa")

        case "detener":
            print("Apagando  sistema...")

        case _:
            # El gion bajo (_) es el comodin. Funciona como el 'default'.
            # Atrapa cualquier cosa que no coincida con los casos de arriba.
            print("ERROR: comando no reconocido.")


# Probamos la funcion
ejecutar_comando("iniciar")
ejecutar_comando("saltar")
