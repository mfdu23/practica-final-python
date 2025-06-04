#Funciones para la interfaz de consola:
from clases.producto import Producto
from clases.cliente import Cliente
from clases.inventario import Inventario
from clases.mascota import Perro, Gato
from clases.venta import Venta


def registrar_mascota():
    tipo = input("Ingrese el tipo de mascota (Gato/Perro): ").strip().lower()
    nombre = input("Ingrese el nombre de la mascota: ")
    edad = int(input("Ingrese la edad de la mascota: "))
    salud = input("Ingrese el estado de salud de la mascota: ")
    precio = float(input("Ingrese el precio de la mascota: "))

    if tipo == "perro":
        raza = input("Ingrese la raza del perro: ")
        nivel_energia = input("Ingrese el nivel de energía del perro: ")
        mascota = Perro(nombre, edad, salud, precio, raza, nivel_energia)
    elif tipo == "gato":
        raza = input("Ingrese la raza del gato: ")
        independencia = input("Ingrese el nivel de independencia del gato: ")
        mascota = Gato(nombre, edad, salud, precio, raza, independencia)
    else:
        print("Tipo de mascota no reconocido.")
        return
    
    return mascota

def registrar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")    
    cliente = Cliente(nombre, direccion, telefono)
    return cliente

def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    producto = Producto(nombre, precio, cantidad, categoria)
    return producto
                       

def registrar_venta(clientes, inventario):
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    productos = []

    while True:
        nombre_producto = input("Ingrese el nombre del producto (deje vacío para finalizar): ")
        if not nombre_producto:
            break
        
        producto = next((p for p in inventario.lista_productos if p.nombre == nombre_producto), None)
        if producto:
            productos.append(producto)
        else:
           print("Producto no encontrado") 

        if productos:
            venta = Venta(cliente, productos)            
            venta.registrar_venta()
            print("La venta se ha registrado exitosamente.")
        else:
            print("No se han agregado productos a la venta.")

def mostrar_menu():
    print("\ --- Menú de gestión de Mascotas ---")
    print("1. Registrar Mascota")
    print("2. Registrar Cliente")
    print("3. Registrar Producto")
    print("4. Registrar Venta")
    print("5. Mostrar Información de Mascotas")
    print("6. Mostrar Información de Clientes")
    print("7. Mostrar Información de Productos")
    print("8. Generar Alerta de Inventario")
    print("9. Salir")

def main():
    mascotas = []
    clientes = []
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mascota = registrar_mascota()
            if mascota:
                mascotas.append(mascota)                
                print("Mascota registrada exitosamente.")

        elif opcion == "2":
            cliente = registrar_cliente()
            if cliente:
                clientes.append(cliente)
                print("Cliente registrado exitosamente.")

        elif opcion == "3":
            producto = registrar_producto()
            if producto:
                inventario.agregar_producto(producto)
                print("Producto registrado exitosamente.")
        
        elif opcion == "4":
            registrar_venta(clientes, inventario)
        
        elif opcion == "5":
            for mascota in mascotas:
                print(mascota.mostrar_informacion())
                if isinstance(mascota, Perro) or isinstance(mascota, Gato):
                    print(mascota.mostrar_caracteristicas())
        
        elif opcion == "6":
            for cliente in clientes:
                print(cliente.mostrar_informacion())
        
        elif opcion == "7":
            for producto in inventario.lista_productos:
                print(producto.mostrar_informacion())
        
        elif opcion == "8":
            umbral_minimo = int(input("Ingrese el umbral mínimo de inventario: "))
            print(inventario.generar_alerta(umbral_minimo))

        elif opcion == "9":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

        
