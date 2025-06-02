class Producto:
    def __init__(self, nombre, precio, cantidad, categoria):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    def actualizar_cantidad(self, cantidad):        
        self.cantidad = cantidad

    def mostrar_informacion(self):
        return f"Producto: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}"