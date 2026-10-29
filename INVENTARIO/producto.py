class Producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print("Venta realizada correctamente.")
        else:
            print("Error: No hay suficiente stock disponible.")

    def mostrarInfo(self):
        print("\n--- INFORMACIÓN DEL PRODUCTO ---")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Stock disponible: {self.stock}")

    def actualizarPrecio(self, nuevoPrecio):
        self.precio = nuevoPrecio
        print("Precio actualizado correctamente.")

    def surtir(self, stockNuevo):
        self.stock += stockNuevo
        print("Stock agregado correctamente.")
