from re import I


class Mascota:
    def __init__(self, nombre, edad, salud, precio  ):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.precio = precio

    def actualizar_informacion(self, nombre=None, edad=None, salud=None, precio=None):
        if nombre is not None:
            self.nombre = nombre
        if edad is not None:
            self.edad = edad
        if salud is not None:
            self.salud = salud
        if precio is not None:
            self.precio = precio

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salud: {self.salud}, Precio: {self.precio}"


class Perro(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, nivel_energia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.nivel_energia = nivel_energia

    def mostrar_caracteristicas(self):
        return f"Raza: {self.raza}, Nivel de Energía: {self.nivel_energia}"  


class Gato(Mascota):
        def __init__(self, nombre, edad, salud, precio, raza, independencia):
            super().__init__(nombre, edad, salud, precio)
            self.raza = raza
            self.independencia = independencia

        def mostrar_caracteristicas(self):
            return f"Raza: {self.raza}, Independencia: {self.independencia}"  