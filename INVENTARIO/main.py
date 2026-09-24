from producto import Producto

if __name__ == "__main__":

    producto = Producto("Laptop", 500, 10)

    while True:

        print("\n===== GESTIÓN DE INVENTARIO =====")
        print("1. Mostrar información")
        print("2. Vender producto")
        print("3. Actualizar precio")
        print("4. Agregar stock")
        print("0. Salir")

        try:
            opcion = int(input("Selecciona una opción: "))

            match opcion:

                case 1:
                    producto.mostrarInfo()

                case 2:
                    cantidad = int(input("¿Cuántos productos deseas vender?: "))
                    producto.vender(cantidad)

                case 3:
                    nuevoPrecio = float(input("Ingresa el nuevo precio: "))
                    producto.actualizarPrecio(nuevoPrecio)

                case 4:
                    stockNuevo = int(input("¿Cuántos productos deseas agregar?: "))
                    producto.surtir(stockNuevo)

                case 0:
                    print("Saliendo del programa...")
                    break

                case _:
                    print("Opción no válida.")

        except ValueError:
            print("Error: debes ingresar un número.")
