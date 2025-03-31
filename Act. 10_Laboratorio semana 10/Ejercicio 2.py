inventario = []

def agregar_producto(nombre, categoria, precio, cantidad):
    inventario.append({"nombre": nombre, "categoria": categoria, "precio": precio, "cantidad": cantidad})

def eliminar_producto(nombre):
    global inventario
    inventario = [producto for producto in inventario if producto["nombre"] != nombre]

def buscar_producto(nombre):
    for producto in inventario:
        if producto["nombre"] == nombre:
            return producto
    return None

def mostrar_inventario():
    inventario_ordenado = sorted(inventario, key=lambda x: x['precio'])
    for producto in inventario_ordenado:
        print(f"{producto['nombre']} - {producto['categoria']} - {producto['precio']} - {producto['cantidad']}")

# Ejemplo de uso:
agregar_producto("Laptop", "Electrónica", 800, 5)
agregar_producto("Smartphone", "Electrónica", 500, 10)
mostrar_inventario()
eliminar_producto("Laptop")
mostrar_inventario()
