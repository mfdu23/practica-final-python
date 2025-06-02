class Inventario:
    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)

    def actualizar_inventario(self, nombre_producto, cantidad):
        for producto in self.lista_productos:
            if producto.nombre == nombre_producto:
                producto.actualizar_cantidad(cantidad)

    def generar_alerta(self, umbral_minimo):
        alertas = [producto.nombre for producto in self.lista_productos if producto.cantidad < umbral_minimo]
        return f"Productos por debajo del umbral: {', '.join(alertas)}" if alertas else "No hay ningún producto por debajo del umbral minimo especificado."