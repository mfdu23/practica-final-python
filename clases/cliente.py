class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historial_compras = []

    def actualizar_informacion(self, nombre=None, direccion=None, telefono=None):
        if direccion is not None:
            self.direccion = direccion
        if telefono is not None:
            self.telefono = telefono
    
    def registrar_compra(self, mascota):
        self.historial_compras.append(mascota)

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"